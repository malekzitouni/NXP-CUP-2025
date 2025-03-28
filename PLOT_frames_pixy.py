from __future__ import print_function
import pixy
from ctypes import *
from pixy import *
import cv2
import numpy as np

# Configuration
PIXY_WIDTH = 316  # Pixy2 native resolution
PIXY_HEIGHT = 208
DISPLAY_WIDTH = 900  # Window size
DISPLAY_HEIGHT = 700

def scale_coords(x, y):
    """Scale Pixy2 coordinates to display size"""
    scale_x = DISPLAY_WIDTH / PIXY_WIDTH
    scale_y = DISPLAY_HEIGHT / PIXY_HEIGHT
    return int(x * scale_x), int(y * scale_y)


def main():
    print("Pixy2 Vector Visualization")
    pixy.init()
    pixy.change_prog("line")  # Line tracking mode for vectors

    # Create display window
    cv2.namedWindow('Pixy2 Vector Visualization', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Pixy2 Vector Visualization', DISPLAY_WIDTH, DISPLAY_HEIGHT)

    # Vector array for storing detected vectors
    vectors = VectorArray(100)

    while True:
        # Create blank image for visualization
        vis_frame = np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH, 3), dtype=np.uint8)

        # Get vectors from Pixy2
        line_get_all_features()
        v_count = line_get_vectors(100, vectors)

        # Draw each vector
        for i in range(v_count):
            x0, y0 = scale_coords(vectors[i].m_x0, vectors[i].m_y0)
            x1, y1 = scale_coords(vectors[i].m_x1, vectors[i].m_y1)

            # Draw vector line (green)
            cv2.line(vis_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)

            # Draw start point (blue)
            cv2.circle(vis_frame, (x0, y0), 3, (255, 0, 0), -1)

            # Draw end point (red)
            cv2.circle(vis_frame, (x1, y1), 3, (0, 0, 255), -1)
        # Show visualization
        cv2.imshow('Pixy2 Vector Visualization', vis_frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()