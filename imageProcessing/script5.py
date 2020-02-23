import cv2, time


video= cv2.VideoCapture(0)

print(type(video))

check, frame = video.read()

print(check)
print(type(frame))
time.sleep(3)
cv2.imshow("capturing video", frame)
cv2.waitKey(0)



cv2.destroyAllWindows()
video.release()



