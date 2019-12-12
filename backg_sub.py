import cv2
import numpy as np
import time
cap=cv2.VideoCapture("car1.avi")
#img=cv2.imread("lane.jpg")
_,firstframe=cap.read()
grayfirst=cv2.cvtColor(firstframe,cv2.COLOR_BGR2GRAY)
while True:
     #_,firstframe=cap.read()
     ret,frame=cap.read()
     if not ret:
          cap=cv2.VideoCapture("car1.avi")
          continue
     grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     #cv2.imshow("dsf",grayfirst)
     diff=cv2.absdiff(grayfirst,grayframe)
     _,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
     #diff=grayframe-grayfirst
     cv2.imshow("dfh",diff)
     #time.sleep(1)
     #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     #corners=cv2.goodFeaturesToTrack(gray,200,0.1,30)
     #print(corners)
     #if corners is not None:
          #corners=np.int0(corners)
          #for corner in corners:
                #x,y=corner.ravel()
                #cv2.circle(frame,(x,y),3,(0,0,255),-1)
     #cv2.imshow("yg",frame)
     if cv2.waitKey(2)==27:
          break
cap.release()
cv2.destroyAllWindows()
     
    
