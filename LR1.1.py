import cv2
import numpy as np

p=False
primitiv = np.array([[255, 255, 0],
                     [255, 255, 0],
                     [0, 0, 0]],  np.uint8)
m0 = np.zeros((3, 3))

cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 300)

while True:
    succes, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY=0?
    #img = cv2.Canny(img, 90, 90)

    if  p==True:
           img = cv2.erode(img, primitiv,iterations = 1)

    cv2.imshow("Image", img)
    k = cv2.waitKey(10)
    if k == ord(' '):
        p=not p
        print(p)

    if k == ord('q'):
        break
