# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:03:48 2018

@author: 瞎砍斗士
"""
import numpy as np
import cv2 as cv
image=cv.imread('C:\\opencv\\1.png');
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY);
sobel = cv.Sobel(gray, cv.CV_8U, 1, 0, ksize = 3);
ret, binary = cv.threshold(sobel, 0, 255, cv.THRESH_OTSU+cv.THRESH_BINARY)
element1 = cv.getStructuringElement(cv.MORPH_RECT, (25, 1))
element2 = cv.getStructuringElement(cv.MORPH_RECT, (25, 1))
dilation = cv.dilate(binary, element2, iterations = 1)
erosion = cv.erode(dilation, element1, iterations = 1)

region=[];
img2, contours, hierarchy = cv.findContours(erosion, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cnt = contours[i];
    area = cv.contourArea(cnt);
    if(area < 1000):
        continue
    rect = cv.minAreaRect(cnt);
    box = cv.boxPoints(rect);
    box = np.int0(box);
    region.append(box);
for box in region:
    cv.drawContours(image, [box], 0, (0, 255, 0), 2)
cv.imshow("1",image);
cv.imwrite("C:\\opencv\\out_1.png",image);
cv.waitKey(5000);
cv.destroyWindow("1");