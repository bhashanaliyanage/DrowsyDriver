import cv2
import winsound


# Checking camera
def check_camera(camera):
    if not camera.isOpened():
        raise IOError("Cannot open camera")

    ret, image = camera.read()
    cv2.imwrite("test_images/image.png", image)
    print("Check test_images folder")


def check_audio():
    winsound.Beep(1000, 1000)
