# Getting libraries
import cv2
import dlib
from imutils import face_utils
import winsound
import matplotlib.pyplot as plt
import testing as test
import computations_drowsy as comp

# Getting webcam
camera_port = 0  # Defining camera port
cam = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)  # Getting camera
# test.check_camera(cam)
# test.check_audio()
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("resources/shape_predictor_68_face_landmarks.dat")  # Getting landmarks
print("Drowsy Driver Detection\nSystem Loaded")

# Key variables (These variables will help for the calculation)
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

######################################################################################################################## Lakshitha

while True:
    # Reading from camera
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)  # Applying DLIB Face detector to the video frame to find out the face in video
    for face in faces:  # Looping over DLIB facial nodes
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)  # Converting facial landmarks to a NUMPY array

        ################################################################################################################ Bhashana

        # Setting the landmarks to detect eyes
        left_blink = comp.blinked(landmarks[36], landmarks[37], landmarks[38], landmarks[41],
                                  landmarks[40], landmarks[39])
        right_blink = comp.blinked(landmarks[42], landmarks[43], landmarks[44], landmarks[47],
                                   landmarks[46], landmarks[45])

        ################################################################################################################ Nishadhi

        # Calculating eye blinks
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 6:
                winsound.Beep(1000, 100)  # Playing a beep sound if user is sleeping
                hist = cv2.calcHist([frame], [0], None, [256], [0, 256])  # Calculating a histogram
                plt.plot(hist)
                plt.savefig("test_images/last_sleep.png")  # Saving the histogram into a file
                status = "User is SLEEPING!!!"
                print("User is Sleeping")
                color = (255, 0, 0)

        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            drowsy += 1
            active = 0
            if drowsy > 6:
                status = "User is DROWSY!!!"
                color = (0, 0, 255)

        else:
            sleep = 0
            drowsy = 0
            active += 1
            if active > 6:
                status = "User is ACTIVE"
                color = (0, 255, 0)

        ################################################################################################################ ROY

        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # Esc button to stop the program
        print("Quitting...")
        break

cam.release()  # Closing camera
cv2.destroyAllWindows()  # Close window

######################################################################################################################## Diunika
