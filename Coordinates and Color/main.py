import cv2 as cv

def click_event(event,x,y,flag,parm):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,"",y)
        font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
        strXY = str(x)+", "+str(y)
        cv.putText(img,strXY,(x,y),font,0.5,(225,55,200),2)
        cv.imshow("image",img)
    
    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
        strBGR = str(blue)+","+str(green)+", "+str(red)
        cv.putText(img,strBGR,(x,y),font,0.5,(100,55,0),2)
        cv.imshow("image",img)



path = "****" #path of photo
img = cv.imread(path)
cv.imshow("image",img)
cv.setMouseCallback("image",click_event)
cv.waitKey(0) 
cv.destroyAllWindows()