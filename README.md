# dorm_door_face_detector

Dependencies:
openCV
numpy
Matplotlib
Pandas (wrapper library to make it easier to call stuff from numpy and matplotlib)
    doc: https://mode.com/python-tutorial/libraries/pandas/
Scikitlearn
    doc: https://scikit-learn.org/stable/install.html



Summary:
MVP
- Detect a single person consistently out of a group of multiple people with a 90% success rate

-Python-
numpy

Steps:
1. Get a face out of a picture (OpenCV library)
2. Put that face into a matrix
3. Write our own eigenfaces algorithm to identify that face
4. Spit out if that face is Joseph or not
