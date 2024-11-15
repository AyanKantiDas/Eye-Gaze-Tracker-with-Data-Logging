
# Eye-Gaze-Tracker-with-Data-Logging

An eye gaze tracking application built using Python and OpenCV, which detects facial features and tracks the direction of gaze in real-time. The application logs data, including timestamps, gaze direction, and on-screen status, and saves it in an Excel file for analysis.


## Features

 - Face and Eye Detection: Utilizes Haar cascades for detecting faces and eyes in real-time.
 - Gaze Direction Analysis: Identifies gaze direction (Left, Right, Up, Down, or Center) and logs whether the user is looking on-screen or off-screen.
 - Data Logging: Saves data into an Excel file, including timestamps, gaze direction, and on-screen status, using the user's name as the file identifier.
 - Real-Time Visualization: Displays the detected face and eyes with bounding boxes on the video feed.


## Installation

Prerequisites

Ensure you have Python installed along with the required libraries:

- OpenCV
- Pandas
- NumPy

### Setup
- Clone this repository:

```bash
git clone https://github.com/your-username/eye-gaze-tracker.git
cd eye-gaze-tracker
```

- Install the required dependencies:

```bash
pip install opencv-python pandas
```

- Ensure your system has a functional webcam.


## Usage

- Run the script:

```bash
python gaze_tracker.py
```

- Enter your full name when prompted. This will be used to name the output file.
- A window will open displaying the real-time video feed with face and eye detection. Press q or Esc to quit.
- After exiting, an Excel file with the logged gaze data will be saved in the current directory:

```bash
<Your_Name>_gaze_data.xlsx
```
## Output
The Excel file contains the following columns:

- Timestamp: The time when the gaze was recorded.
- Gaze Direction: Detected direction of the gaze (e.g., Left, Right, Up, Down, Center).
- On_Screen: Boolean indicating whether the gaze was detected on-screen (True) or off-screen (False).
## Customization
- Gaze Direction Sensitivity: Adjust thresholds for gaze classification in the detect_gaze_direction() function.
- Data Columns: Modify the gaze_data DataFrame to include additional metrics if needed.
- Save Location: Change the output directory for the Excel file by updating the file_name variable.
## Known Limitations
- Performance may vary depending on lighting conditions and webcam quality.
- Gaze detection relies on the accuracy of Haar cascades, which may not handle all edge cases.
## Acknowledgments
- OpenCV for computer vision libraries.
- Haar Cascade Classifiers for face and eye detection.
- Pandas for data management and Excel export functionality.
Happy tracking! 😊