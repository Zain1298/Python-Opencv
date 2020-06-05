import cv2

img = cv2.imread('sz.jpeg')

cv2.imshow('Output Image',img)




cv2.waitKey(0)


cv2.destroyAllWindows()
#destroyAllWindows function destroys or closes all the windows when the any key is pressed.
