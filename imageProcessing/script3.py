import cv2

face_cascade = cv2.CascadeClassifier(r"classifiers\haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img,
scaleFactor=1.05,
minNeighbors=5)


print(type(faces))
print(faces)
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+w), (0,255,0), 3)

    
cv2.imshow("face detected image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




