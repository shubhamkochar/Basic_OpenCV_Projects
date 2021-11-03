import cv2 as cv

path = "Enter video path"
cap = cv.VideoCapture(path)
count = 1

if(cap.isOpened()==False):
    print("Error in opening video file.")

while(cap.isOpened()):
    ret,frame = cap.read()

    if ret == True:
        cv.imshow("video",frame)
        cv.imwrite("Images%d.jpg"%count,frame)
        print("Image frame",count,"saved.")
        count+=1

        if cv.waitKey(1)& 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()