#define a class

import numpy as np
import cv2


# initialize the camera
def camcapture():
    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    for i in range(10):
        s, img = cam.read()
    s, img = cam.read()

    if s:    # frame captured without any errors
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)


        return gray



    

    

