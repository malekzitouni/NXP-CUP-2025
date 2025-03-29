from __future__ import print_function
import pixy
from ctypes import *
from pixy import *
import time
import math

# Configuration parameters
angular_velocity = -0.5  # Steering gain (negative for correct direction)
linear_velocity = 0.7  # Base speed (unused in servo-only control)
single_line_steer_scale = 0.6  # Smoother steering for single lines
MAX_SERVO_ANGLE = 40  # Maximum servo angle in degrees
STEER_DEADZONE = 0.1  # Minimum steer value to move servo

# Global variables
steer = 0.0  # Current steering value (-1.0 to 1.0)


def __init__():
    """Initialize Pixy2 camera"""
    pixy.init()
    pixy.change_prog("line")
    print("Pixy2 initialized in line tracking mode")


def set_servo_angle(angle):
    """Set servo to specified angle (in degrees) with safety limits"""
    # Constrain angle to valid range
    constrained_angle = max(-MAX_SERVO_ANGLE, min(MAX_SERVO_ANGLE, angle))

    # Platform-specific servo control would go here
    # Example for Raspberry Pi:
    # duty_cycle = 7.5 + (constrained_angle / 18)  # Convert angle to duty cycle
    # pwm_servo.ChangeDutyCycle(duty_cycle)

    print(f"Servo angle set to: {constrained_angle:.1f}°")


def collect_pixy_data():
    """Get vector data and calculate steering"""
    global steer  # Use the global steer variable

    line_get_all_features()
    vectors = VectorArray(100)
    v_count = line_get_vectors(100, vectors)

    # Debug print vectors
    print(f"\nFound {v_count} vectors:")
    for i in range(v_count):
        print(f"Vector {i}: ({vectors[i].m_x0},{vectors[i].m_y0}) to ({vectors[i].m_x1},{vectors[i].m_y1})")

    if v_count > 1:
        # Two vectors detected (junction or parallel lines)
        x0_0, y0_0 = vectors[0].m_x0, vectors[0].m_y0
        x1_0, y1_0 = vectors[0].m_x1, vectors[0].m_y1
        x0_1, y0_1 = vectors[1].m_x0, vectors[1].m_y0
        x1_1, y1_1 = vectors[1].m_x1, vectors[1].m_y1

        window_center = get_frame_width() / 2

        if (x0_1 >= x1_1) and (x0_0 <= x1_0):
            midpoint = (x1_0 + x1_1) / 2.0
            steer = angular_velocity * ((midpoint - window_center) / get_frame_width())
        elif (x0_1 < x1_1) and (x0_0 <= x1_0):
            midpoint = (x1_0 + x0_1) / 2.0
            steer = angular_velocity * ((midpoint - window_center) / get_frame_width())
        elif (x0_1 > x1_1) and (x0_0 > x1_0):
            midpoint = (x0_0 + x1_1) / 2.0
            steer = angular_velocity * ((midpoint - window_center) / get_frame_width())
        else:
            midpoint = (x0_0 + x0_1) / 2.0
            steer = angular_velocity * ((midpoint - window_center) / get_frame_width())

    elif v_count == 1:
        # Single vector detected (normal line following)
        x0_0, y0_0 = vectors[0].m_x0, vectors[0].m_y0
        x1_0, y1_0 = vectors[0].m_x1, vectors[0].m_y1

        if x1_0 > x0_0:
            dx = (x1_0 - x0_0) / get_frame_width()
            dy = (y1_0 - y0_0) / get_frame_height()
        else:
            dx = (x0_0 - x1_0) / get_frame_width()
            dy = (y0_0 - y1_0) / get_frame_height()

        if (x0_0 != x1_0) and (abs(dy) > 0.001):  # Avoid division by tiny numbers
            slope = dx / dy
            steer = -angular_velocity * slope * single_line_steer_scale
            print(f"Line slope: {slope:.2f}")
        else:
            steer = 0.0  # Vertical line or invalid slope
    else:
        print("No lines detected - stopping")
        steer = 0.0

    # Apply dead_zone to prevent servo jitter
    if abs(steer) < STEER_DEADZONE:
        steer = 0.0

    return steer
'''
if steer<0 then turn left 
else if steer>0 then turn right
'''

if __name__ == "__main__":
    try:
        __init__()
        while True:
            current_steer = collect_pixy_data()
            servo_angle = steer * MAX_SERVO_ANGLE
            set_servo_angle(servo_angle)

            print(f"Steer: {current_steer:.2f}, Servo: {servo_angle:.1f}°")
            time.sleep(0.1)  # 10Hz update rate for smoother control

    except KeyboardInterrupt:
        print("\nCentering servo and exiting...")
        set_servo_angle(0)  # Center servo on exit