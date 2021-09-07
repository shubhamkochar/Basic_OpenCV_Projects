# In this we going to find the black and white dots in a image.

import cv2 as cv

def nothing(x):
    print(x)                                                            

path = "****" #Enter image path
img = cv.imread(path)
print(img.shape)
img = cv.resize(img,[720,520])
cv.namedWindow("Threshold")

cv.createTrackbar("Threshold value","Threshold",0,255,nothing)

while(1):
    th = cv.getTrackbarPos("Threshold value","Threshold")
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    _,mask = cv.threshold(gray,th,255,cv.THRESH_BINARY_INV)
    cv.imshow("Dots position",mask)
    cv.imshow("Original Image",img)
    k = cv.waitKey(1) &0xFF
    if k ==27:
        break

cv.destroyAllWindows()


