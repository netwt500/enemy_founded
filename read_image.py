import cv2

image =cv2.imread('./image/lunar_eclipse.jpg')

h,w,c=image.shape
print(h,w,c)
cv2.imshow("Image", image)
cv2.waitKey()
cv2.destroyAllWindows()