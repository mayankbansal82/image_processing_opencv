import cv2
import numpy as np
cap=cv2.VideoCapture("challenge.mp4")
#img=cv2.imread("lane.jpg")
while True:
     ret,frame=cap.read()
     if not ret:
          cap=cv2.VideoCapture("challenge.mp4")
          continue
     img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     h,w=img_gray.shape
     vertices=np.array([[0,h],[w/2,h/2],[w,h]],np.int32)
     edges=cv2.Canny(img_gray,75,150)
     #cv2.imshow("rfg",edges)
     mask=np.zeros_like(edges)
     cv2.fillPoly(mask,[vertices],255)
     #cv2.imshow("rf",mask)
     masked=cv2.bitwise_and(edges,mask)
     #cv2.imshow("sf",masked)
     lines=cv2.HoughLinesP(masked,1,np.pi/180,150,maxLineGap=500,minLineLength=500)
     #print(lines)
     if lines is not None:
          for line in lines:
               x1,y1,x2,y2=line[0]
               cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
          cv2.imshow("cd",frame)
     if cv2.waitKey(1)==27:
          break
cap.release()
cv2.destroyAllWindows()
     
    
