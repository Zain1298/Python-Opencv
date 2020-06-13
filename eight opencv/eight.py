import cv2
import numpy as np

img = cv2.imread("black.png")
height,width = img.shape[:2]
print(height)
print(width)


rotation_img =cv2.getRotationMatrix2D((width/2,height/2),180,.5)
rotation_image = cv2.warpAffine(img , rotation_img, (width,height))
print(rotation_image)
print(rotation_img)

cv2.imshow('Original Image',img)
cv2.imshow('Rotation Image',rotation_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
