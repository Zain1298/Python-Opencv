import cv2
import numpy as np

img = cv2.imread("black.png")

height,width = img.shape[:2]
print(height)
print(width)

quarter_height,quarter_width = height/4 , width/4
print(quarter_height)
print(quarter_width)

T = np.float32([[1,0,quarter_height],[0,1,quarter_width]])
print(T)

img_translation = cv2.warpAffine(img,T,(width,height))
cv2.imshow('Original Image', img)
cv2.imshow('Translation', img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()