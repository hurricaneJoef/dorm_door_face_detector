# dorm_door_face_detector

Dependencies:
openCV
    doc: https://docs.opencv.org/4.5.4/
numpy
    install: https://numpy.org/install/
Matplotlib
    installation: https://matplotlib.org/stable/users/installing.html
Pandas (wrapper library to make it easier to call stuff from numpy and matplotlib)
    doc: https://mode.com/python-tutorial/libraries/pandas/
Scikitlearn
    installation: https://scikit-learn.org/stable/install.html



Summary:
MVP
- Detect a single person consistently out of a group of multiple people with a 90% success rate

-Python-
numpy


for help:

https://towardsdatascience.com/eigenfaces-face-classification-in-python-7b8d2af3d3ea


Steps:
1. Get a face out of a picture (OpenCV library)
2. Put that face into a matrix
3. Write our own eigenfaces algorithm to identify that face
4. Spit out if that face is Joseph or not

State machine:

3 states --
1. Camera
2. isface
3. isme

