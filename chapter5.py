import cv2
import numpy as np
img = cv2.imread("C:/Users/harik/OneDrive/Desktop/OpenCV/Resources/playing-cards.jpg")
width, height=250,350
pts1=np.float32([[595,108], [815,204], [450, 456], [674, 553]])
pts2=np.float32([[0, 0],[width, 0],[0, height],[width, height]])
matrix=cv2.getPerspectiveTransform(pts1, pts2)
imgOutput=cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Output", imgOutput)
cv2.imshow("Image", img)
cv2.waitKey(0)