# IMPORTING ALL THE NECESSARY DEPENENCIES AND LIBRARIES
import numpy as np
import cv2
from matplotlib import pyplot as plt

#READING THE IMAGE
img = cv2.imread('heregoesyouamazingimage')

#CREATING A MASK USING NUMPY
mask = np.zeros(img.shape[:2],np.uint8)

#DEFINIGN THE FOREGROUND AND BACKGROUND MODELS
background_model = np.zeros((1,65),np.float64)
foreground_model = np.zeros((1,65),np.float64)

#THE FOUR PARAMETERS REPRESENTS STARTING OF X, STARTING OF Y, WIDTH AND HEIGHT RESPECTIVELY
#THE COORDINATES CHANGES AS THE IMAGE CHANGES
rectangle = (161,79,150,150)

#APPLYING THE GRABCUT FUNCTION WITH APPROPRIATE PARAMETERS
cv2.grabCut(img,mask,rectangle,background_model,foreground_model,5,cv2.GC_INIT_WITH_RECT)

#CREATE MASK WHERE SURE AND LIKELY BACKGROUNDS SET TO 0, OTHERWISE 1
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

#MULTIPLY IMAGE WITH NEW MASK TO SUBTRACT BACKGROUND
img = img*mask2[:,:,np.newaxis]

#OUPUT THE FINAL RESULTING IMAGE
plt.imshow(img)
plt.colorbar()
plt.show()