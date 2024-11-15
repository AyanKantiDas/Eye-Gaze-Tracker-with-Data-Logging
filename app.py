import cv2
import pandas as pd
from datetime import datetime
import os


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


user_name = input("Enter full name: ")
file_name = f"{user_name.replace(' ', '_')}_gaze_data.xlsx"


gaze_data = pd.DataFrame(columns=['Timestamp', 'Gaze Direction', 'On_Screen'])


cap = cv2.VideoCapture(0)

def detect_gaze_direction(eye_region):
    _, thresholded_eye = cv2.threshold(eye_region, 30, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresholded_eye, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        pupil_contour = max(contours, key=cv2.contourArea)
        (px, py, pw, ph) = cv2.boundingRect(pupil_contour)
        center_x, center_y = px + pw / 2, py + ph / 2
        width, height = eye_region.shape[1], eye_region.shape[0]

      
        if center_x < width * 0.3:
            return 'Left'
        elif center_x > width * 0.7:
            return 'Right'
        elif center_y < height * 0.3:
            return 'Up'
        elif center_y > height * 0.7:
            return 'Down'
        else:
            return 'Center'
    else:
        return 'Off_Screen'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            eye_region = roi_gray[ey:ey+eh, ex:ex+ew]
            gaze_direction = detect_gaze_direction(eye_region)
            on_screen = gaze_direction != 'Off_Screen'

            gaze_data = pd.concat([gaze_data, pd.DataFrame([{
                'Timestamp': datetime.now(),
                'Gaze Direction': gaze_direction,
                'On_Screen': on_screen
            }])], ignore_index=True)

            cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)

    cv2.imshow('Eye Tracking', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:  # 'q' or 'Esc' to exit
        break

# Save the data to an Excel file with the user’s name in the filename
gaze_data.to_excel(file_name, index=False)

cap.release()
cv2.destroyAllWindows()
