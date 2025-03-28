# drivebot_style_controller.py
import pygame
import time
import sys


class DriveBotController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 480))
        pygame.display.set_caption("NXP_Cup Keyboard Controller")

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (150, 150, 150)
        self.LIGHT_GRAY = (200, 200, 200)
        self.HIGHLIGHT = (100, 200, 255)

        # Fonts
        self.title_font = pygame.font.Font(None, 48)
        self.subtitle_font = pygame.font.Font(None, 24)
        self.button_font = pygame.font.Font(None, 32)

        # Control state
        self.steering = 0
        self.throttle = 0
        self.max_speed = 0.5
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

    def draw_display(self):
        # White background
        self.screen.fill(self.WHITE)

        # Title and subtitle
        title = self.title_font.render("Nxp_Cup Keyboard Controller", True, self.BLACK)
        subtitle = self.subtitle_font.render("Use Arrow Keys to Move | Space to Stop", True, self.BLACK)

        self.screen.blit(title, (540 - title.get_width() // 2, 25))
        self.screen.blit(subtitle, (540 - subtitle.get_width() // 2, 80))

        # Draw buttons
        for btn_name, rect in self.buttons.items():
            color = self.LIGHT_GRAY if btn_name == self.active_button else self.GRAY
            pygame.draw.rect(self.screen, color, rect, border_radius=10)

            # Button labels
            if btn_name == 'forward':
                text = self.button_font.render("FORWARD", True, self.BLACK)
                self.screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))
            elif btn_name == 'backward':
                text = self.button_font.render("BACKWARD", True, self.BLACK)
                self.screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))
            elif btn_name == 'left':
                text = self.button_font.render("LEFT", True, self.BLACK)
                self.screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))
            elif btn_name == 'right':
                text = self.button_font.render("RIGHT", True, self.BLACK)
                self.screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))
            elif btn_name == 'stop':
                text = self.button_font.render("STOP (SPACE)", True, self.BLACK)
                self.screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

        # Display current values
        status_text = f"Throttle: {self.throttle:.2f} | Steering: {self.steering:.2f}"
        status = self.subtitle_font.render(status_text, True, self.BLACK)
        self.screen.blit(status, (540 - status.get_width() // 2, 400))

        pygame.display.flip()

    def get_controls(self):
        self.steering = 0
        self.throttle = 0
        self.active_button = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.throttle = self.max_speed
            self.active_button = 'forward'
            print("ROBOT IS MOVING FORWARD")
        elif keys[pygame.K_DOWN]:
            self.throttle = -self.max_speed * 0.5
            self.active_button = 'backward'
            print("ROBOT IS MOVING BACKWARD")

        if keys[pygame.K_LEFT]:
            self.steering = 0.5
            self.active_button = 'left'
            print("ROBOT IS TAKING LEFT TURN")
        elif keys[pygame.K_RIGHT]:
            self.steering = -0.5
            self.active_button = 'right'
            print("ROBOT IS TAKING RIGHT TURN")

        if keys[pygame.K_SPACE]:
            self.throttle = 0
            self.steering = 0
            self.active_button = 'stop'
            print("ROBOT HAS STOPPED")

        return {'steering': self.steering, 'throttle': self.throttle}

    def run_controller(self):
        print("DriveBot Controller Initialized")
        print("Use Arrow Keys to control, Space to stop")

        clock = pygame.time.Clock()

        while self.running:
            controls = self.get_controls()
            self.draw_display()
            clock.tick(30)

        pygame.quit()
        print("Controller shutdown")














































if __name__ == "__main__":
    controller = DriveBotController()
    controller.run_controller()
    sys.exit()