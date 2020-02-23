import cv2

face_cascade = cv2.CascadeClassifier(r"D:\imageProcessing\classifiers\haarcascade_frontalface_default.xml")

img = cv2.imread(r"D:\imageProcessing\photo.jpg", 1)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img,
scaleFactor=1.05,
minNeighbors=5)

print(type(faces))
print(faces)

cv2.imshow("grey image window",grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


