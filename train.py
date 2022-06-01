import cv2 as cv
import numpy as np
cap = cv.VideoCapture('/Users/local/PycharmProjects/train/3686.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    grayed = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    dst = cv.Canny(grayed, 00, 50, None, 3)
    blurred = cv.blur(dst, (5, 5))


    thresh = 10
    #img_bw = cv.threshold(blurred, thresh, 255, cv.THRESH_BINARY)[1]
    cv.circle(frame, (700, 1000), 20, (0,255,0), -1)
    cv.imshow("asd", frame)
    if cv.waitKey(30) == ord(' '):
        break




cap.release()
cv.destroyAllWindows()
