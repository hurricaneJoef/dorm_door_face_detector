from numpy import linalg as LA
import numpy as np
import cv2 as cv2
import os

from numpy.core.fromnumeric import size
'''def traineig()
    with open('trainingdata.npy', 'rb') as f:
        a = np.load(f)#subject id
'''
def eigtrain(eigennumber):
    eigentrainimgs = [[]]
    dim = (64,64)
    for filename in os.listdir('trainingdata/cropped'):
        cimg = cv2.imread(os.path.join('trainingdata/cropped', filename))
        img = cv2.cvtColor(cv2.resize(cimg, dim, interpolation = cv2.INTER_AREA), cv2.COLOR_BGR2GRAY)#resize
        print(img.shape)
        try:
            eigentrainimgs = np.append(eigentrainimgs,np.ubyte(img.reshape((img.size,1))),1)
        except Exception:
            eigentrainimgs = np.ubyte(img.reshape((img.size,1)))
    eigmean = np.mean(eigentrainimgs,axis=1)
    eigenmean = eigmean.reshape((eigmean.size,1))
    eigenmeancentered = eigentrainimgs - eigenmean
    print("eigen yeet")
    print(np.mean(eigenmeancentered))
    eigN = np.shape(eigenmeancentered)[0]
    a = np.matmul(eigenmeancentered,eigenmeancentered.T)/np.sqrt(eigN-1)
    print(a.shape)
    w, v = LA.eigh(a) #make eig weigts and vectors
    print('v shape')
    print(v.shape)
    besteignum = (-1-eigenmeancentered)
    with open('eigenvectorsbest.npy','wb') as f:
        np.save(f,v[-41:-1,:])
    with open('eigenmean.npy','wb') as f:
        np.save(f,eigenmean)
'''
to load these eigen vectors

with open('eigenvectorsbest.npy','rb') as f:
        eigenvectors = np.load(f)

thats all you need

'''

if __name__ == "__main__":
    eigtrain(40)