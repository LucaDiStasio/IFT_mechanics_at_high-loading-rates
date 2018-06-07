# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2016-2018 Université de Lorraine & Luleå tekniska universitet
Author: Luca Di Stasio <luca.distasio@gmail.com>
                       <luca.distasio@ingpec.eu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

=====================================================================================

DESCRIPTION

Image analysis of Double Cantilever Beam test recordings.

Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution
       in Windows 10.

'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

def getLowerProfile(binImage):
    coords = []
    height,width = binImage.shape
    
    for c in range(0,len(binImage[0,:])):
        whites = []
        for r,row in enumerate(binImage[:,c]):
            if binImage[r,c]>0:
                whites.append(r)
        if len(whites)>0:
            coords.append([c,height-np.max(whites)])
    coords = np.array(coords)
    return coords

def getUpperProfile(binImage):
    coords = []
    height,width = binImage.shape
    
    for c in range(0,len(binImage[0,:])):
        whites = []
        for r,row in enumerate(binImage[:,c]):
            if binImage[r,c]>0:
                whites.append(r)
        if len(whites)>0:
            coords.append([c,height-np.min(whites)])
    coords = np.array(coords)
    return coords

def getMeanProfile(binImage):
    coords = []
    height,width = binImage.shape
    
    for c in range(0,len(binImage[0,:])):
        whites = []
        for r,row in enumerate(binImage[:,c]):
            if binImage[r,c]>0:
                whites.append(r)
        if len(whites)>0:
            coords.append([c,height-np.mean(whites)])
    coords = np.array(coords)
    return coords
    
    
plt.close('all')

img = cv2.imread('LAM365-1-s-0329_0.tif',0)
height,width = img.shape

img2 = img.copy()

template = cv2.imread('lower-hinge.tif',0)
w, h = template.shape[::-1]

template2 = cv2.imread('upper-hinge.tif',0)
w2, h2 = template2.shape[::-1]

template3 = cv2.imread('crack-tip.tif',0)
w3, h3 = template3.shape[::-1]

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

res2 = cv2.matchTemplate(img,template2,cv2.TM_CCOEFF_NORMED)
min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)

top_left2 = max_loc2
bottom_right2 = (top_left2[0] + w2, top_left2[1] + h2)

res3 = cv2.matchTemplate(img,template3,cv2.TM_CCOEFF_NORMED)
min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(res3)

top_left3 = max_loc3
bottom_right3 = (top_left3[0] + w3, top_left3[1] + h3)

cv2.rectangle(img,top_left, bottom_right, 255, 4)
cv2.rectangle(img,top_left2, bottom_right2, 255, 4)
cv2.rectangle(img,top_left3, bottom_right3, 255, 4)

upperArm = img2[int(np.floor(0.5*(top_left2[1]+bottom_right2[1]))):int(np.ceil(0.5*(top_left3[1]+bottom_right3[1]))),int(np.floor(0.5*(top_left2[0]+bottom_right2[0]))):int(np.ceil(0.5*(top_left3[0]+bottom_right3[0])))]

ret,upperArmBin = cv2.threshold(upperArm,127,255,cv2.THRESH_BINARY)

upperArmCoords = getLowerProfile(upperArmBin)

lowerArm = img2[int(np.floor(0.5*(top_left3[1]+bottom_right3[1]))):int(np.ceil(0.5*(top_left[1]+bottom_right[1]))),int(np.ceil(0.5*(top_left[0]+bottom_right[0]))):int(np.ceil(0.5*(top_left3[0]+bottom_right3[0])))]

ret,lowerArmBin = cv2.threshold(lowerArm,127,255,cv2.THRESH_BINARY)

lowerArmCoords = getUpperProfile(lowerArmBin)

rearArm = img2[int(np.floor(0.5*(top_left2[1]+bottom_right2[1]))):int(np.ceil(0.5*(top_left[1]+bottom_right[1]))),int(np.ceil(0.5*(top_left3[0]+bottom_right3[0]))):]

ret,rearArmBin = cv2.threshold(rearArm,127,255,cv2.THRESH_BINARY)

rearArmCoords = getMeanProfile(rearArmBin)

plt.subplot(3,3,1)
plt.imshow(upperArm,cmap = 'gray')
plt.title('Upper arm')
plt.xticks([])
plt.yticks([])
plt.subplot(3,3,2)
plt.imshow(upperArmBin,cmap = 'gray')
plt.title('Binarized')
plt.xticks([])
plt.yticks([])
plt.subplot(3,3,3)
plt.plot(upperArmCoords[:,0],upperArmCoords[:,1],'b.')
plt.title('Coordinates plot')
plt.subplot(3,3,4)
plt.imshow(lowerArm,cmap = 'gray')
plt.title('Lower arm')
plt.xticks([])
plt.yticks([])
plt.subplot(3,3,5)
plt.imshow(lowerArmBin,cmap = 'gray')
plt.title('Binarized')
plt.xticks([])
plt.yticks([])
plt.subplot(3,3,6)
plt.plot(lowerArmCoords[:,0],lowerArmCoords[:,1],'b.')
plt.title('Coordinates plot')
plt.subplot(3,3,7)
plt.imshow(rearArm,cmap = 'gray')
plt.title('Rear arm')
plt.xticks([])
plt.yticks([])
plt.subplot(3,3,8)
plt.imshow(rearArmBin,cmap = 'gray')
plt.title('Binarized')
plt.xticks([])
plt.yticks([])
plt.subplot(3,3,9)
plt.plot(rearArmCoords[:,0],rearArmCoords[:,1],'b.')
plt.title('Coordinates plot')

plt.figure()
plt.imshow(img,cmap = 'gray')
plt.title('Detected Points')
plt.xticks([])
plt.yticks([])
plt.show()

#cv2.imwrite('trial.png',img)
#ret,th = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

#surf = cv2.SURF(30000)
#kp, des = surf.detectAndCompute(th,None)
#print len(kp)
#img2 = cv2.drawKeypoints(th,kp,None,(255,0,0),4)

#edges = cv2.Canny(img,100,200)

#cv2.line(img,(0,0),(width,height),(0,0,255),5)

#imageTitle = 'Double Cantilever Beam Test'

#cv2.namedWindow(imageTitle)

#fig, (ax1, ax2, ax3) = plt.subplots(1,3)
#ax1.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#ax2.imshow(th, cmap = 'gray')
#ax2.imshow(img2)
#ax3.imshow(edges, cmap='gray')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.tight_layout()
#plt.show()
