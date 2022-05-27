import cv2 as cv
import numpy as np
cap = cv.VideoCapture('3686.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    grayed = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    dst = cv.Canny(grayed, 50, 300, None, 3)
    blurred = cv.blur(dst, (20, 20))


    thresh = 10
    img_bw = cv.threshold(blurred, thresh, 255, cv.THRESH_BINARY)[1]
    cv.imshow("asd", img_bw)
    if cv.waitKey(30) == ord(' '):
        break




cap.release()
cv.destroyAllWindows()
