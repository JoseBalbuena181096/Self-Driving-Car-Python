#!/usr/bin/env python 
import cv2
import numpy as np 

def canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def display_lines(image,lines):
    #create array with zero (black color) with the row x columns of image for a new image
    line_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            #unpack the coordinates of each line
            x1,y1,x2,y2=line.reshape(4)
            #add  the line to the image line image
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image


def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([
        (200,height),(1100,height),(550,250)
    ])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,[polygons],255)
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image


image=cv2.imread("test_image.jpg")
lane_image=np.copy(image)
canny_image=canny(lane_image)
cropped_image=region_of_interest(canny_image)
#Apply Probabilist Hough Transform
#cv2.HoughLineP(image_cany,rho_acuracie,theta_acuracie,array_for_output,minLineLength,maxLineGap)
lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
line_image=display_lines(lane_image,lines)
#add line to color image
combo_image=cv2.addWeighted(lane_image,0.8,line_image,1,1) 
cv2.imshow("Line Image",combo_image)
cv2.waitKey(0)
