import cv2

img = cv2.imread('sz.jpg')

cv2.imshow('Output Image',img)

print(img.shape)
#print image shape in tuple form (height,width,layersofRGB)

print("Value of Height:",img.shape[0])
print("Value of Width:",img.shape[1])
print("How many layers in a pic :",img.shape[2])

cv2.waitKey(0)

cv2.destroyAllWindows()

