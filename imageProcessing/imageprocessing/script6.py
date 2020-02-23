import cv2

video = cv2.VideoCapture(r"D:\imageProcessing\faceDetection.mp4")
face_cascade = cv2.CascadeClassifier(r"D:\imageProcessing\classifiers\haarcascade_frontalface_default.xml")
# print(type(video))
check = True
while check:

    check, frame = video.read()

    cv2.imshow("video ka first frame", frame)
    key = cv2.waitKey(10)
    if(key == ord('q')):
        break
cv2.destroyAllWindows()
video.release()