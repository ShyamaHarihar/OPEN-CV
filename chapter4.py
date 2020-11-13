import cv2
import numpy as np
img=np.zeros((512, 512,3),np.uint8)
#size of the image which is filled with zeroes
print(img)
img[:]=255, 0, 0
cv2.line(img , (0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),cv2.FILLED)
cv2.putText(img,"OPEN CV",(300,100),cv2.FONT_ITALIC,1,(0,255,0),2)#cropping width and height width first and then height
cv2.imshow("Image", img)
#0 means black
cv2.waitKey(0)