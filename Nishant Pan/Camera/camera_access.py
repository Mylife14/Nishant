import cv2
cap = cv2.VideoCapture('http://192.168.246.238:8080/video')
while True:
    ret, frame = cap.read()
    resized = cv2.resize(frame,(600,400))
    cv2.imshow("Frame", resized)

    key = cv2.waitkey(1)
    if key == ord("q"):
        break
    