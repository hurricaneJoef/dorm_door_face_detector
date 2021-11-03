#facecrop.py

import numpy as np
import cv2
def crop2face(gimg):
    #crop input image to largest face
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    
    # Detect faces
    #print(gimg)

    cv2.imshow("cam-test",gimg)

    faces = face_cascade.detectMultiScale(gimg, 1.1, 4)
    
    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(gimg, (x, y), (x+w, y+h), (255), 2)
        faceimg = gimg[y:y + h, x:x + w]
        return faceimg
        
    # Display the output
    
    #cv2.imshow('gimg', gimg)
    #cv2.waitKey()
    #return gimg