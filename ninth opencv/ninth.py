import cv2

img = cv2.imread("black.png")

rotated_image = cv2.transpose(img)

cv2.imshow("Original Image", img)
cv2.imshow("Transpose Image", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()