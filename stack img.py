import cv2
import numpy as np

img = cv2.imread("sample.jpg")

imgBlue = img[:,:,0]       
imgGreen = img[:,:,1]         
imgRed = img[:,:,2]             

new_img = np.hstack((imgBlue, imgGreen, imgRed))

cv2.imshow("window",new_img)     #SHOW THE IMAGE
cv2.waitKey(0)                   #SO THAT IT WAITS ON THE WINDOW
