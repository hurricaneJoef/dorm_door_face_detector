from camerapro import *

img = camcapture()
cv2.namedWindow("cam-test")
cv2.imshow("cam-test",img)
cv2.waitKey(0)
cv2.destroyWindow("cam-test") 
