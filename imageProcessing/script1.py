import cv2 

img1 = cv2.imread('galaxy.jpg',0)

print(type(img1))
print(img1)
print(img1.shape)
print(img1.ndim) 
resized_img1 = cv2.resize(img1, (int(img1.shape[1]/2), int(img1.shape[0]/2)))

cv2.imshow("FIRST IMAGE", resized_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


