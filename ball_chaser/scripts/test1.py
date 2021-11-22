#!/usr/bin/env python


import numpy as np
import numpy
import cv2
 

image_name = "track_view"

print('read an image from file')
img = cv2.imread(image_name+".png")


print('create a window holder for the image')
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)
cv2.waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print('create a window holder for the image')
cv2.imshow("Image",hsv)
cv2.waitKey(0)

lower_yellow = numpy.array([ 10,  10,  10])
upper_yellow = numpy.array([255, 255, 250])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
print('create a window holder for the image')
cv2.imshow("Image",mask)
cv2.waitKey(0)

h, w, d = img.shape
search_top = int(3*h/4)
search_bot = int(3*h/4 + 20)
mask[0:search_top, 0:w] = 0
mask[search_bot:h, 0:w] = 0
print('create a window holder for the image')
cv2.namedWindow("Image1",cv2.WINDOW_NORMAL)
cv2.imshow("Image1",mask)
cv2.waitKey(0)

M = cv2.moments(mask)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv2.circle(mask, (cx, cy), 20, (128,128,128), -1)
cv2.imshow("Image1",mask)
cv2.waitKey(0)


cv2.circle(img, (cx, cy), 20, (0,0,255), -1)
print('create a window holder for the image')
cv2.namedWindow("Image2",cv2.WINDOW_NORMAL)
cv2.imshow("Image2",img)
cv2.waitKey(0)



