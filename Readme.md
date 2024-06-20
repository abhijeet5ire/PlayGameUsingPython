# Pose Detection and Control with MediaPipe, OpenCV, and PyAutoGUI

This project utilizes the MediaPipe library to detect human poses via webcam feed and triggers keyboard actions using PyAutoGUI based on the detected pose. The primary actions mapped are "defend" (`w` key) and "punch" (`space` key).

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/your_username/pose-detection-control.git
    cd pose-detection-control
    ```

2. Install the required packages:
    ```sh
    pip install mediapipe opencv-python numpy pyautogui
    ```

## Usage

Run the script to start the webcam feed and pose detection:

```sh
python gameplay.py

Hello 