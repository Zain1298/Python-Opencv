import cv2

img = cv2.imread('sz.jpg',0)

cv2.imshow("Original Image",img)

cv2.waitKey(0)

ret, bw = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

#white pixels are above 100
#black pixels are below 100

cv2.imshow("Binary Image",bw)

cv2.waitKey(0)


cv2.destroyAllWindows()