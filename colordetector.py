
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([110, 50, 50])
    upper_red = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break


# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

# release the captured frame
cap.release()