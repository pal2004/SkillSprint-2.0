
import cv2
import datetime as dt

cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outout.avi',fourcc,50,(640,480),True)

while True:
    ret, frame = cap.read()
    print(frame.shape)
    date_time=str(dt.datetime.now())+' Shephali'
    frame=cv2.putText(frame,date_time,(10,450),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow("Video",frame)
    
    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
