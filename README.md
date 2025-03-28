# NXP-CUP-2025
Here is a README file for the `StoreVectorsSteering.py` script based on the provided script and repository information:

```markdown
# StoreVectorsSteering

This repository contains a Python script `StoreVectorsSteering.py` for data collection using the Pixy2 camera and Pygame for a graphical user interface. The script is designed for the NXP Cup competition, where it collects and stores vector data detected by the Pixy2 camera.

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

```

This README file provides an overview of the script, installation instructions, usage details, and additional information about the data collection process.
