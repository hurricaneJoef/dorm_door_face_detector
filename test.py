from camerapro import *
from facecrop import * 
import numpy as np
import cv2 as cv
import os.path


img = camcapture()
cv2.namedWindow("cam-test")
cv2.imshow("cam-test",img)

try:
    with open('trainedfaced.npy', 'rb') as f:
        facestrained =  np.load(f)#subject id
except FileNotFoundError:
    facestrained = 0

try:
    os.mkdir('trainingdata')
    os.mkdir('trainingdata/cropped')
except Exception:
    pass

faces = crop2face(img)
cv2.namedWindow("face-test")
cv2.imshow("face-test",faces)
cv2.imwrite(os.path.join('trainingdata','cropped','img'+str(facestrained)+'.png'),faces)

cv2.imwrite(os.path.join('trainingdata','img'+str(facestrained)+'.png'),img)

facestrained+=1
with open('trainedfaced.npy', 'wb') as f:
    np.save(f,facestrained )#subject id


cv2.waitKey(0)
cv2.destroyWindow("cam-test") 
try:
    cv2.destroyWindow("face-test")
except Exception:
    None
print(facestrained)