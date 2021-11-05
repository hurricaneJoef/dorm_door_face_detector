from camerapro import *
from facecrop import *

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as pltfrom 

from numpy import linalg as LA
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report

from PIL import Image
import warnings
warnings.filterwarnings('ignore')

#to be deleted once we can pass an image in through another function
img = camcapture()   
 
def isme(img):
    
    dim = (64,64)
    with open('eigenvectorsbest.npy','rb') as f:
        eigenvectors = np.load(f)
    
    for filename in os.listdir('correctfaces'):
        mytimg = cv2.imread(os.path.join('correctfaces', filename))
        
        meis = cv2.resize(mytimg, dim, interpolation = cv2.INTER_AREA)#resize
        try:
            correcteigs = np.append(correcteigs,np.ubyte(meis.reshape((meis.size,1))),1)
        except Exception:
            correcteigs = np.ubyte(meis.reshape((meis.size,1)))

    cvec = np.true_divide(correcteigs,eigenvectors)
    print(cvec.shape)

    timg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)#resize
    tarray = np.ubyte(timg.reshape((timg.size,1)))
    tvec = np.true_divide(timg,eigenvectors)
    print(tvec.shape)

    for column in correcteigs.T:
        tarray.square + column.square
    
    
    
    

