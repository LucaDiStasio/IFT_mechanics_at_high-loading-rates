# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2016 Université de Lorraine & Luleå tekniska universitet
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

img = cv2.imread('LAM365-1-s-0329_0.tif',0)
height,width = img.shape

#cv2.imwrite('trial.png',img)
ret,th = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

surf = cv2.SURF(30000)
kp, des = surf.detectAndCompute(th,None)
print len(kp)
img2 = cv2.drawKeypoints(th,kp,None,(255,0,0),4)

edges = cv2.Canny(img,100,200)

#cv2.line(img,(0,0),(width,height),(0,0,255),5)

#imageTitle = 'Double Cantilever Beam Test'

#cv2.namedWindow(imageTitle)

fig, (ax1, ax2, ax3) = plt.subplots(1,3)
ax1.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#ax2.imshow(th, cmap = 'gray')
ax2.imshow(img2)
ax3.imshow(edges, cmap='gray')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.tight_layout()
plt.show()
