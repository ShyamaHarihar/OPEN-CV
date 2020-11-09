import cv2
print('Package Imported')
cap=cv2.VideoCapture("C:/Users/harik/OneDrive/Desktop/OpenCV/Resources/video-1.mp4")
#13:04
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
