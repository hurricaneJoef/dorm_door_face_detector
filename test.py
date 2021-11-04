from camerapro import *
from facecrop import *


img = camcapture()
cv2.namedWindow("cam-test")
cv2.imshow("cam-test",img)


faces = crop2face(img)
cv2.namedWindow("face-test")
cv2.imshow("face-test",faces)
cv2.waitKey(0)
cv2.destroyWindow("cam-test") 
cv2.waitKey(0)
cv2.destroyWindow("face-test") 