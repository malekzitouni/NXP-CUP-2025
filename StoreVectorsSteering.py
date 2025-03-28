from __future__ import print_function
import pygame
import pixy
from ctypes import *
from pixy import *
import csv
import os
from datetime import datetime
import time
import sys
import servo_control
#maxThrottle = 0.25
class DataCollectionController:
    def __init__(self):
        # Initialize Pixy
        pixy.init()
        pixy.change_prog("line")

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 480))
        pygame.display.set_caption("NXP_Cup Data Collector")

        # UI Configuration
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (150, 150, 150)
        self.LIGHT_GRAY = (200, 200, 200)
        self.HIGHLIGHT = (100, 200, 255)

        self.title_font = pygame.font.Font(None, 48)
        self.subtitle_font = pygame.font.Font(None, 24)
        self.button_font = pygame.font.Font(None, 32)

        # Control state
        self.steering = 0
        self.throttle = 0
        self.max_speed = 0.5
        self.steering_step = 0.02  # Increment per frame while holding
        self.running = True
        self.active_button = None

        # Button rectangles
        self.buttons = {
            'forward': pygame.Rect(755, 125, 100, 100),
            'backward': pygame.Rect(755, 250, 100, 100),
            'left': pygame.Rect(630, 250, 100, 100),
            'right': pygame.Rect(880, 250, 100, 100),
            'stop': pygame.Rect(100, 250, 400, 100)
        }

        # Data collection setup
        self.output_dir = os.path.expanduser("~/Desktop/Pixy_Data")
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        self.csv_filename = os.path.join(
            self.output_dir,
            f"pixy_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        # Initialize CSV file
        with open(self.csv_filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                'frame',
                'steering', 'throttle',
                'vector_index', 'x0', 'y0', 'x1', 'y1', 'flags'
            ])

        print(f"Data collection initialized. Saving to: {self.csv_filename}")
        self.frame = 0

    def draw_display(self):
        # Your original display code (unchanged)
        self.screen.fill(self.WHITE)

        title = self.title_font.render("Nxp_Cup Data Collector", True, self.BLACK)
        subtitle = self.subtitle_font.render("Use Arrows to Control | SPACE=Stop | ESC=Exit", True, self.BLACK)

        self.screen.blit(title, (540 - title.get_width() // 2, 25))
        self.screen.blit(subtitle, (540 - subtitle.get_width() // 2, 80))

        for btn_name, rect in self.buttons.items():
            color = self.LIGHT_GRAY if btn_name == self.active_button else self.GRAY
            pygame.draw.rect(self.screen, color, rect, border_radius=10)

            if btn_name == 'forward':
                text = self.button_font.render("FORWARD", True, self.BLACK)
            elif btn_name == 'backward':
                text = self.button_font.render("BACKWARD", True, self.BLACK)
            elif btn_name == 'left':
                text = self.button_font.render("LEFT", True, self.BLACK)
            elif btn_name == 'right':
                text = self.button_font.render("RIGHT", True, self.BLACK)
            elif btn_name == 'stop':
                text = self.button_font.render("STOP (SPACE)", True, self.BLACK)

            self.screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

        # Enhanced status display with frame counter
        status_text = f"Frame: {self.frame} | Throttle: {self.throttle:.2f} | Steering: {self.steering:.2f}"
        status = self.subtitle_font.render(status_text, True, self.BLACK)
        self.screen.blit(status, (540 - status.get_width() // 2, 400))

        pygame.display.flip()

    def get_controls(self):
        # Reset active button
        self.active_button = None

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        keys = pygame.key.get_pressed()

        # Throttle control (unchanged)
        if keys[pygame.K_UP]:
            self.throttle = self.max_speed
            self.active_button = 'forward'
        elif keys[pygame.K_DOWN]:
            self.throttle = -self.max_speed * 0.5
            self.active_button = 'backward'
        elif keys[pygame.K_SPACE]:
            self.throttle = 0
            self.steering = 0  # Reset steering when stopping
            self.active_button = 'stop'

        # Steering control (modified for gradual increase)
        if keys[pygame.K_LEFT]:
            self.steering = min(self.steering + self.steering_step, 0.5)  # Increase left steering
            self.active_button = 'left'
        elif keys[pygame.K_RIGHT]:
            self.steering = max(self.steering - self.steering_step, -0.5)  # Increase right steering
            self.active_button = 'right'
        elif not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            # Reset steering when no keys pressed
            if abs(self.steering) < 0.01:  # Deadzone to avoid tiny values
                self.steering = 0
            else:
                # Gradual return to center
                self.steering *= 0.9  # Smooth decay

        return {'steering': self.steering, 'throttle': self.throttle}

    def collect_pixy_data(self):
        # Get Pixy vector data
        line_get_all_features()
        vectors = VectorArray(100)
        v_count = line_get_vectors(100, vectors)

        # Write to CSV
        with open(self.csv_filename, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            timestamp = datetime.now().strftime("%H:%M:%S.%f")

            if v_count > 0:
                for index in range(v_count):
                    writer.writerow([

                        self.frame,
                        self.steering,
                        self.throttle,
                        vectors[index].m_index,
                        vectors[index].m_x0,
                        vectors[index].m_y0,
                        vectors[index].m_x1,
                        vectors[index].m_y1,
                        vectors[index].m_flags
                    ])
            else:
                # Log even when no vectors detected
                writer.writerow([
                    self.frame,
                    self.steering,
                    self.throttle,
                    -1,  # No vector indicator
                    0, 0, 0, 0, 0
                ])

        return v_count

    def run(self):
        clock = pygame.time.Clock()
        print("Data collection started. Use arrow keys to control...")

        try:
            while self.running:
                # Get controls and update display
                controls = self.get_controls()
                self.draw_display()

                # Collect and log data
                v_count = self.collect_pixy_data()
                print(
                    f"Frame {self.frame}: Steering={self.steering:.2f}, Throttle={self.throttle:.2f}, Vectors={v_count}")

                self.frame += 1
                clock.tick(30)  # ~30 FPS

        except KeyboardInterrupt:
            pass
        finally:
            pygame.quit()
            print(f"\nData collection complete. Saved {self.frame} frames to:\n{self.csv_filename}")
            sys.exit()


if __name__ == "__main__":
    controller = DataCollectionController()
    controller.run()
    #servo_control.move()
