import cv2
import numpy as np
img = cv2.imread("C:/Users/harik/OneDrive/Desktop/OpenCV/Resources/img1.png")
print(img.shape)
#width then height
imgResize=cv2.resize(img,(300,200))
print(imgResize.shape)
imgCropped=img[0:200 ,200:500]
#height first then the width
cv2.imshow("Image", img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)
