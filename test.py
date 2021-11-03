from camerapro import *
from facecrop import *


img = camcapture()
cv2.namedWindow("cam-test")
cv2.imshow("cam-test",img)
cv2.waitKey(0)
cv2.destroyWindow("cam-test") 

faces = crop2face(camcapture())
cv2.namedWindow("cam-test")
cv2.imshow("cam-test",faces)
cv2.waitKey(0)
cv2.destroyWindow("cam-test") 