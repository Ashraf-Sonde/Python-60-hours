import cv2

img = cv2.imread(r'D:\imageProcessing\galaxy.jpg',0)

print(type(img))
print(img)
print(img.shape)    
height = img.shape[0]
width = img.shape[1]
resized_height = int(height/2)
resized_Width = int(width/2)

resized_image = cv2.resize(img, (resized_Width, resized_height))

cv2.imwrite("new_galaxy.jpg", resized_image)

cv2.imshow("galaxy image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
172.16.104.50