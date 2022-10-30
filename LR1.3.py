import time
import cv2
import numba
import numpy as np

@numba.jit()
def func_equal(a, b):
    y1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    y2 = np.zeros((3, 3))
    k=0
    for i in range(0,3):
        for j in range(3):
            if a[i][j] == b[i][j]:
                  k += 1
    if k == 9:
        y=255
    else:
        y=0
    return y


primitiv = np.array([[255, 255, 255],
                     [255, 255, 255],
                     [255, 255, 255]])
m0 = np.zeros((3, 3))
p=0
cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 300)

while True:

    img = cv2.imread('image_1.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY=0?
    #print(img.shape)
  #  img = cv2.Canny(img, 90, 90)
    i = 0
    j = 0
  #print(img.shape)
    if p:
        start_time = time.time()
        n0 = np.zeros(img.shape)
        while i < img.shape[0] -1:
            while j < img.shape[1] - 1:

                n0[i+1][j+1]=func_equal(img[i:i + 3, j:j + 3],primitiv[0:3, 0:3])
                j=j+1
            i = i + 1
            j = 0
        img = n0
        print("Execution time of the program is- ", time.time()-start_time)
    cv2.imshow("result", img)
    #cv2.imwrite('1.3_result.jpg')
    k = cv2.waitKey(0)
    if k == ord('q'):
        #cv2.imwrite('1.3_result.jpg')
        break
    if k == ord(' '):
        p = not p
        print(p)


