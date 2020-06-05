import cv2

img = cv2.imread('sz.jpeg')

cv2.imshow('Output Image',img)


cv2.imwrite('Output.jpg',img)
cv2.imwrite('Output.png',img)

cv2.waitKey(0)

cv2.destroyAllWindows()

