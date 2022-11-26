# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kRnNrafHFb4lb8J9OaQ3joPj5nPIxaW0
"""

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = cv2.imread('Macaron_noise.jpg', 0)
imgplot = plt.imshow(img,cmap='gray', vmin=0, vmax=255)
plt.show()


import numpy as np

imgSrc=img.copy()
padded = np.pad(imgSrc, pad_width = 1, mode = 'constant') 
paddedCopy=padded
count=0

for i in range(1,751):
  for j in range(1,751):
    fil=np.zeros(0)
    for f in range(i-1,i+2):
      for g in range(j-1,j+2):
        fil=np.append(fil,padded[f][g])
    med=np.median(fil)
    if((padded[i][j]==0 or padded[i][j]==255) and med<255 and med>0):
      count+=1
    paddedCopy[i][j]=med
print(count)

cv2.imwrite('new3_1.jpg',paddedCopy)

padded = paddedCopy
for i in range(1,751):
  for j in range(1,751):
    fil=np.zeros(0)
    for f in range(i-1,i+2):
      for g in range(j-1,j+2):
        fil=np.append(fil,padded[f][g])
    med=np.median(fil)
    if((padded[i][j]==0 or padded[i][j]==255) and med<255 and med>0):
      count+=1
    paddedCopy[i][j]=med
print(count)

cv2.imwrite('new3_2.jpg',paddedCopy)

for i in range(1,76):
  for j in range(1,76):
    fil=np.zeros(0)
    for f in range(i-1,i+2):
      for g in range(j-1,j+2):
        fil=np.append(fil,padded[f][g])
    med=np.median(fil)
    if((padded[i][j]==0 or padded[i][j]==255) and med<255 and med>0):
      count+=1
    paddedCopy[i][j]=med
count

imgSrc=img.copy()
padded5 = np.pad(imgSrc, pad_width = 2, mode = 'constant') 
padded5Copy=padded5
print(count5)=0

for i in range(1,751):
  for j in range(1,751):
    fil=np.zeros(0)
    for f in range(i-2,i+3):
      for g in range(j-2,j+3):
        fil=np.append(fil,padded5[f][g])
    med=np.median(fil)
    if((padded5[i][j]==0 or padded5[i][j]==255) and med<255 and med>0):
      count5+=1
    padded5Copy[i][j]=med
print(count5)

cv2.imwrite('new5.jpg',padded5Copy)

for i in range(1,76):
  for j in range(1,76):
    fil=np.zeros(0)
    for f in range(i-2,i+3):
      for g in range(j-2,j+3):
        fil=np.append(fil,padded5[f][g])
    med=np.median(fil)
    if((padded5[i][j]==0 or padded5[i][j]==255) and med<255 and med>0):
      count5+=1    
    padded5Copy[i][j]=med
print(count5)
