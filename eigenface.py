from camerapro import *
from facecrop import *

import numpy as np 

from numpy import linalg as LA, true_divide
import os

import warnings
warnings.filterwarnings('ignore')

#to be deleted once we can pass an image in through another function
 
 
def isme(img):
    
    dim = (64,64)
    with open('eigenvectorsbest.npy','rb') as f:
        eigenvectors = np.load(f)
    with open('eigenmean.npy','rb') as f:
        eigenmean = np.load(f)
    
    for filename in os.listdir('correctfaces'):
        mytimg = cv2.imread(os.path.join('correctfaces', filename))
        
        meis = cv2.cvtColor(cv2.resize(mytimg, dim, interpolation = cv2.INTER_AREA), cv2.COLOR_BGR2GRAY)#resize
        #print(meis.shape)
        try:
            correcteigs = np.append(correcteigs,np.ubyte(meis.reshape((meis.size,1))),1)
        except Exception:
            correcteigs = np.ubyte(meis.reshape((meis.size,1)))
    mcorrecteigs = correcteigs               -eigenmean
    #print(mcorrecteigs.shape)
    cvec,cresid,crank,cs = np.linalg.lstsq(eigenvectors.T,mcorrecteigs)
    #print(cvec.shape)

    bruhimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)#resize
    timg  = bruhimg.reshape((bruhimg.size,1))         -eigenmean
    tarray = np.ubyte(timg.reshape((timg.size,1)))
    tvec,tresid,trank,ts = np.linalg.lstsq(eigenvectors.T,timg)
    #print(tvec.shape)
    i=0
    for column in cvec.T:
        
        distsq = np.sum(np.square(tvec-column.T.reshape(column.size,1)))
        #print("lillian was here")
        #print(column.T.shape)
        print(distsq)
        if np.min(distsq) < 40000:
            '''cimg = np.multiply(column,eigenvectors.T).resize((64,64))
            cv2.namedWindow("cvec-test")
            cv2.imshow("cvec-test",cimg)
            cv2.waitKey(0)
            cv2.namedWindow("tvec-test")
            cv2.imshow("tvec-test",bruhimg)
            cv2.waitKey(0)
            cv2.destroyWindow("tvec-test")
            cv2.destroyWindow("cvec-test")  #'''
            return True
        i += 1
    return False
            
    
    
    
    
if __name__ == "__main__":
    face = None
    while face is None:
        img = camcapture()
        face = crop2face(img)
        None#'''r
    
    cv2.namedWindow("isme-test")
    cv2.imshow("isme-test",face)
    cv2.waitKey(0)
    cv2.destroyWindow("isme-test") 
    output = isme(face)
    print("output")
    print(output)
    for filename in os.listdir('trainingdata/cropped'):
        face = cv2.cvtColor( cv2.imread("trainingdata/cropped/"+filename) , cv2.COLOR_BGR2GRAY)
        print(filename)
        cv2.namedWindow("isme-test")
        cv2.imshow("isme-test",face)
        cv2.waitKey(0)
        cv2.destroyWindow("isme-test") 
        output = isme(face)
        print("output")
        print(output)
