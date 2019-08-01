#!/usr/bin/env python
import cv2
import numpy as np 
image=cv2.imread("test_image.jpg")
#lane_image=image #is the same that next
lane_image=np.copy(image)
#convert rgb image to gray
gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
cv2.imshow("result",gray)
cv2.waitKey(0)