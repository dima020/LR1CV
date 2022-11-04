import cv2
import numpy as np
from PIL import Image
from numpy import count_nonzero

# def qqq(img1, img2):
#     img1k=asarray(img1)
#     img2k=asarray(img2)
#     k = 0
#     for i in img1k.shape[0]:
#         for j in img1k.shape[1]:
#             if img1k[i, j] == img2k[i, j]:
#                 k = k + 1
#     return 1 - k / (img1k.shape[0] * img1k.shape[1])


img1 = cv2.imread('outputs/1.1_result.jpg')
img2 = cv2.imread('outputs/1.2_result.jpg')
img3 = cv2.imread('outputs/1.3_result.jpg')

img12 = cv2.imread('outputs/2.1_result.jpg')
img22= cv2.imread('outputs/2.2_result.jpg')
img32 = cv2.imread('outputs/2.3_result.jpg')

img13 = cv2.imread('outputs/3.1_result.jpg')
img23 = cv2.imread('outputs/3.2_result.jpg')
img33 = cv2.imread('outputs/3.3_result.jpg')


result = np.array(img1-img2)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))

result = np.array(img1-img3)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))

result = np.array(img2-img3)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))


result = np.array(img12-img22)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))

result = np.array(img12-img32)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))

result = np.array(img22-img32)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))

##
result = np.array(img13-img23)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))

result = np.array(img13-img33)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))

result = np.array(img23-img33)
result1=count_nonzero(result)
print(result1/(result.shape[0]*result.shape[1]))




