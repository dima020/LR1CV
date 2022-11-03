import cv2
import numpy as np
from PIL import Image
from numpy import asarray

def qqq(img1, img2):
    img1k=asarray(img1)
    img2k=asarray(img2)
    k = 0
    for i in img1k.shape[0]:
        for j in img1k.shape[1]:
            if img1k[i, j] == img2k[i, j]:
                k = k + 1
    return 1 - k / (img1k.shape[0] * img1k.shape[1])


img1 = cv2.imread('outputs/1.1_result.jpg')
img2 = cv2.imread('outputs/2.3_result.jpg')
img3 = cv2.imread('outputs/1.3_result.jpg')

img = Image.open('outputs/1.1_result.jpg')


#result = qqq(img1,img2)
result1 = cv2.matchTemplate(img1, img3, cv2.TM_CCOEFF_NORMED)

print(result1)

