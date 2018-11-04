#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 15:08:05 2018

@author: weiwei
"""
import numpy as np
import cv2 as cv
video=cv.VideoCapture('/home/weiwei/data/2.mp4')
ret,frame=video.read();
while(video.isOpened()):
    ret,frame=video.read();
    if ret==True:  
        cv.imshow('2',frame);
        frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY);
        frame=cv.Canny(frame,20,25)
        cv.imshow('1',frame);
        cv.waitKey(25);
cv.destroyAllWindows();
video.release();
