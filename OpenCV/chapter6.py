import cv2
import numpy as np
img = cv2.imread('C:/Users/harik/OneDrive/Desktop/OpenCV/Resources/img1.png')
imgHor=np.hstack((img, img))
imgVer=np.vstack((img,img))
cv2.imshow("Horizontal Stacking",imgHor)
cv2.imshow("Horizontal Stacking",imgVer)
cv2.waitKey(0)