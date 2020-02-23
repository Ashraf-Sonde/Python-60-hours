import cv2


eyes_cascade = cv2.CascadeClassifier(r"classifiers\haarcascade_eye.xml")

img = cv2.imread("photo.jpg")

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


eyes = eyes_cascade.detectMultiScale(grey_img,
scaleFactor=1.05,
minNeighbors=6)

print(type(eyes))
print(eyes)

for x, y, w, h in eyes:
    img = cv2.rectangle(img, (x,y), (x+w, y+w), (0,255,0), 3)


cv2.imshow("Grey image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()




