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
    
   
    with open('eigenface.npy', 'wb') as f:
        vectors = np.load(f)#subject id
    
    w, v = LA.eig() #make eig weigts and vectors
    
    
    
    

