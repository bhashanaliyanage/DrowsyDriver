import cv2


# Checking camera
def check_camera(camera):
    if not camera.isOpened():
        raise IOError("Cannot open camera")

    ret, image = camera.read()
    cv2.imwrite("test_images/image.png", image)
    print("Check test_images folder")
