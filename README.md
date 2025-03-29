# NXP-CUP-2025
Here is a README file for the `StoreVectorsSteering.py` script based on the provided script and repository information:

# StoreVectorsSteering

This repository contains a Python script `StoreVectorsSteering.py` for data collection using the Pixy2 camera and Pygame for a graphical user interface. The script is designed for the NXP Cup competition, where it collects and stores vector data detected by the Pixy2 camera.
![Capture d’écran du 2025-03-28 23-47-53](https://github.com/user-attachments/assets/5534eefc-fde5-4dd8-aea9-530c1f8e5504)


## Prerequisites

- Python 3.x
- Pygame library
- Pixy2 Python API
- csv library (part of the Python standard library)
- datetime library (part of the Python standard library)
- os library (part of the Python standard library)
- ctypes library (part of the Python standard library)
- sys library (part of the Python standard library)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/malekzitouni/NXP-CUP-2025.git
   cd NXP-CUP-2025
   ```

2. Install the required libraries:

   ```sh
   pip install pygame
   ```

3. Ensure that the Pixy2 Python API is set up correctly on your system. Refer to the Pixy2 documentation for installation instructions.

## Usage

1. Connect the Pixy2 camera to your computer.

2. Run the `StoreVectorsSteering.py` script:

   ```sh
   python StoreVectorsSteering.py
   ```

3. Use the arrow keys to control the throttle and steering:

   - UP arrow: Move forward
   - DOWN arrow: Move backward
   - LEFT arrow: Turn left
   - RIGHT arrow: Turn right
   - SPACE: Stop

4. The collected data will be saved to a CSV file in the `~/Desktop/Pixy_Data` directory. The filename will include the current date and time.

## Script Details

The `StoreVectorsSteering.py` script initializes the Pixy2 camera and Pygame for the GUI. It displays control buttons and status information on the screen. The script continuously collects vector data from the Pixy2 camera and stores it in a CSV file along with the current frame, throttle, and steering values.

### Control State

- `self.steering`: Current steering value
- `self.throttle`: Current throttle value
- `self.max_speed`: Maximum speed
- `self.steering_step`: Increment per frame while holding the steering keys
- `self.running`: Boolean indicating if the script is running
- `self.active_button`: Currently active button

### Data Collection

- The script collects vector data from the Pixy2 camera using the `line_get_vectors` function.
- The collected data is written to a CSV file with the following columns:
  - `frame`
  - `steering`
  - `throttle`
  - `vector_index`
  - `x0`
  - `y0`
  - `x1`
  - `y1`
  - `flags`

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Pixy2 Camera](https://pixycam.com/pixy2/)
- [Pygame](https://www.pygame.org/)



# PLOT_frames_pixy.py

The PLOT_frames_pixy.py script visualizes vector data detected by the Pixy2 camera using OpenCV. It initializes the Pixy2 camera in line tracking mode to detect vectors and creates a display window to show these vectors in real-time. The script scales the coordinates from the Pixy2 camera's resolution to the display window's resolution and draws the vectors as lines with start and end points on the window. The visualization continues until the user presses the 'q' key to exit.
This README file provides an overview of the script, installation instructions, usage details, and additional information about the data collection process.
![image](https://github.com/user-attachments/assets/10fda4a4-90a8-4af2-a350-31a2bfd6fe8d)


## keyboard.py

The `keyboard.py` script is a keyboard-based controller for the NXP Cup robot. It utilizes the Pygame library to create a graphical user interface (GUI) that allows users to control the robot's movement using keyboard inputs. The script features a display window with control buttons for moving the robot forward, backward, left, right, and stopping it. The script continuously checks for keyboard inputs and updates the robot's throttle and steering values accordingly.

### Key Features

- **Graphical User Interface (GUI)**: A Pygame window is created with buttons representing the control commands.
- **Keyboard Controls**:
  - **Arrow Keys**: Control the robot's movement.
    - UP arrow: Move forward
    - DOWN arrow: Move backward
    - LEFT arrow: Turn left
    - RIGHT arrow: Turn right
  - **Space Bar**: Stop the robot.
  - **ESC Key**: Exit the controller.
- **Real-time Display**: The GUI shows the current throttle and steering values.
- **Control State**: The script maintains and updates the control state, including throttle, steering, and active buttons.
- **Event Handling**: The script handles keyboard events and updates the display accordingly.

### Initialization

The `DriveBotController` class initializes the Pygame environment, sets up the display window, defines colors and fonts, and initializes control states and button rectangles.

### Main Loop

The `run_controller` method contains the main loop, which continuously checks for keyboard inputs, updates the control states, and redraws the display. The loop runs at approximately 30 frames per second.

### Methods

- **draw_display**: Draws the control buttons and status information on the display window.
- **get_controls**: Handles keyboard inputs and updates the throttle and steering values based on the pressed keys.

### Usage

To run the script, simply execute the `keyboard.py` file. The script will initialize the controller and open the Pygame window, ready to accept keyboard inputs for controlling the robot.
![Capture d’écran du 2025-03-28 23-43-34](https://github.com/user-attachments/assets/4fe76bfa-6df1-4000-bbaa-e0502d96007f)



## nxp_cup2024.py

The `nxp_cup2024.py` script is designed to control the steering of a robot using vector data from the Pixy2 camera. The script initializes the Pixy2 camera in line tracking mode and collects vector data to calculate the steering angle. The calculated steering angle is then used to set the position of a servo motor, which controls the robot's direction.

### Key Features

- **Pixy2 Camera Initialization**: The script initializes the Pixy2 camera and sets it to line tracking mode.
- **Collecting Vector Data**: The script collects vector data from the Pixy2 camera and calculates the appropriate steering angle based on the detected vectors.
- **Steering Calculation**:
  - If two vectors are detected, the script calculates the midpoint between the vectors and adjusts the steering angle accordingly.
  - If a single vector is detected, the script calculates the slope of the line and adjusts the steering angle to follow the line.
  - If no vectors are detected, the script stops the steering.
- **Servo Control**: The script sets the servo motor to the calculated steering angle, with safety limits applied to avoid over-rotation.
- **Dead Zone**: A dead zone is applied to the steering value to prevent jittering of the servo motor.

### Configurable Parameters

- **angular_velocity**: Steering gain, with a negative value for the correct direction.
- **linear_velocity**: Base speed (unused in servo-only control).
- **single_line_steer_scale**: Smoother steering for single lines.
- **MAX_SERVO_ANGLE**: Maximum servo angle in degrees.
- **STEER_DEADZONE**: Minimum steer value required to move the servo.

### Usage

1. Ensure the Pixy2 camera is connected to your system.
2. Run the script:

   ```sh
   python nxp_cup2024.py
   ```

3. The script will initialize the Pixy2 camera and continuously collect vector data to calculate and adjust the steering angle. The current steering value and servo angle will be printed to the console.

4. To stop the script, press `Ctrl+C`. The servo will be centered before the script exits.

### Example Output

```
Pixy2 initialized in line tracking mode
Found 2 vectors:
Vector 0: (x0_0, y0_0) to (x1_0, y1_0)
Vector 1: (x0_1, y0_1) to (x1_1, y1_1)
Steer: 0.25, Servo: 10.0°
...
Centering servo and exiting...
Servo angle set to: 0.0°
```

This section provides an overview of the `nxp_cup2024.py` script, including its features, configurable parameters, usage instructions, and example output.
