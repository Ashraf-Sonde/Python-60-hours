import cv2, time

video= cv2.VideoCapture(0)
while True:
    print(type(video))

    check, frame = video.read()

    print(check)
    print(type(frame))
    # time.sleep(3)
    cv2.imshow("capturing video", frame)
    key = cv2.waitKey(10)

    if key == ord('q'):
        break


cv2.destroyAllWindows()
video.release()

