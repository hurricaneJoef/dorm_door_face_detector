from os import write
from camerapro import *
from facecrop import *

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as pltfrom 

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report

from PIL import Image
import warnings
warnings.filterwarnings('ignore')


#to be deleted once we can pass an image in through another function
img = camcapture()
 
#writing the image to a file
cv2.imwrite("face.png", img)


#copied from Pillow -- changing an image to an array
imgsubstep = Image.open("face.png")
imgSequence = imgsubstep.getdata()
imgArray = np.array(img)
np.savetxt("imgMatrix.csv", imgArray, delimiter=",")


#reading that array as a CSV file... might be unnecssary if I can just do it in here
df = pd.read_csv("imgMatrix.csv")
df.head()
print(df.shape)

