import cv2
import mediapipe as mp
import time

#capturing video
cap=cv2.VideoCapture("test2.mp4")

#this will help us detect the pose and draw the reference points
mpPose=mp.solutions.pose
pose=mpPose.Pose()
mpDraw=mp.solutions.drawing_utils

#variables required to print frame rate
previous_time=0
current_time=0

#video
while True:
    success, img=cap.read()
    
    #converting image to rgb
    img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results=pose.process(img_rgb)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    
    #calculating the frame rate
    current_time=time.time()
    frame_rate=1/(current_time-previous_time)
    previous_time=current_time
    
    #displaying the results
    cv2.putText(img, str(int(frame_rate)), (20, 40), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    cv2.imshow("camera", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break