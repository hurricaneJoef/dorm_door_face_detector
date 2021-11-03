#define a class

import numpy as np
from cv2 import *


# initialize the camera
def camcapture():
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()

    if s:    # frame captured without any errors
        namedWindow("cam-test")
        imshow("cam-test",img)
        waitKey(0)
        destroyWindow("cam-test")  


def grayscale(rgb):
    
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gscale = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gscale

#return grayscale picture

def gscalepic():
    return grayscale(camcapture())



    

    

