#!/usr/bin/env python
import cv2
import numpy as np 
#import image
image=cv2.imread("test_image.jpg")
#copy image to lane_image
lane_image=np.copy(image)
#convert image rgb to gray scale
gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
#smoothing image with the filter gaussian
blur=cv2.GaussianBlur(gray,(5,5),0) 
#obtaining the thereshold  
canny=cv2.Canny(blur,50,150)
cv2.imshow("thereshold",canny)
cv2.waitKey(0)
