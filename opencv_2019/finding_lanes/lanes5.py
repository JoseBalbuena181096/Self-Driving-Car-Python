#!/usr/bin/env python
import cv2
import numpy as np 

def canny(image):
    #convert to gray
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    #apply filter for smoothing image
    blur=cv2.GaussianBlur(gray,(5,5),0)
    #apply canny for obtaining the threshold
    canny=cv2.Canny(blur,50,150)
    return canny
#funtion for create the mask with the interest area
def region_of_interest(image):
    #number of rows of the image
    height=image.shape[0]
    #array with the points of the triangle 
    polygons=np.array([
        (200,height),(1100,height),(550,250)
    ])
    #mask with only zeros(color black) ,with rows and colums like image
    mask=np.zeros_like(image)
    #add the triangle with color white(255) to the mask
    cv2.fillPoly(mask,[polygons],255)
    return mask

image=cv2.imread("test_image.jpg")
lane_image=np.copy(image)
canny=canny(lane_image)
region_interest=region_of_interest(canny)
cv2.imshow("mask",region_interest)
cv2.waitKey(0)

