import cv2 as cv
import numpy as np


def nothing(x):
    pass

img = np.zeros((312,512,3),np.uint8)
cv.namedWindow("Trackbar")

cv.createTrackbar("Blue","Trackbar",0,255,nothing)
cv.createTrackbar("Green","Trackbar",0,255,nothing)
cv.createTrackbar("Red","Trackbar",0,255,nothing)

while(1):
    cv.imshow("Color Palette",img)
    k = cv.waitKey(1)
    if k ==27:
        break

    B = cv.getTrackbarPos("Blue","Trackbar")
    G = cv.getTrackbarPos("Green","Trackbar")
    R = cv.getTrackbarPos("Red","Trackbar")

    img[:]= [B,G,R]

cv.destroyAllWindows()


