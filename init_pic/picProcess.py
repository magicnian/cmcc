#!/usr/bin/env python
# --*-- coding:utf-8 --*--

import cv2
import os

output_path = 'E:\\processpic\\cmcc\\'

if __name__ == '__main__':
    path = 'E:\\sourcepic\\cmcc\\'
    for i in range(3000):
        img = cv2.imread(path+str(i)+'.png')
        if img is not None:
            GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(GrayImage, (5, 5), 0)  # 高斯滤波
            ret, thresh3 = cv2.threshold(blurred, 165, 255, cv2.THRESH_BINARY)
            cv2.imwrite(output_path+str(i)+'.png', thresh3)