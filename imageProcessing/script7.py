import cv2, time


face_cascade = cv2.CascadeClassifier(r"classifiers\haarcascade_frontalface_default.xml")

video= cv2.VideoCapture(0)
while True:

    check, frame = video.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey,
    scaleFactor=1.25,
    minNeighbors=14)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+w), (0,255,0), 3)
    cv2.imshow("capturing video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
video.release()



bit.ly/pythonday7