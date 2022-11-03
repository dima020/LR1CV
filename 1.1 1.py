import cv2
import numpy as np
import time
p=False
primitiv = np.array([[255, 255, 255],
                     [255, 255, 255],
                     [255, 255, 255]],  np.uint8)
m0 = np.zeros((3, 3))


while True:
    img = cv2.imread('image_3.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY=0?
    #img = cv2.Canny(img, 90, 90)

    if  p==True:
           start_time=time.time()
           img = cv2.erode(img, primitiv,iterations = 1)
           print("Execution time of the program is- ", time.time() - start_time)
    cv2.imshow("Image", img)
    cv2.imwrite('outputs/3.1_result.jpg', img)
    k = cv2.waitKey(10)
    if k == ord(' '):
        p=not p
        print(p)

    if k == ord('q'):

        break
