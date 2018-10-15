import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascade.xml')
video_capture = cv2.VideoCapture(0)
scale_factor = 1.3
font = cv2.FONT_HERSHEY_DUPLEX
color = (255, 255, 255)
font_black = (0, 0, 0)

while 1:
    ret, pic = video_capture.read()
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
    for(x, y, w, h) in faces:  # x, y, width, height
        cv2.rectangle(pic, (x, y), (x + w, y + h), color, 2)
        cv2.putText(pic, 'Face', (x, y), font, 2, font_black, 2, cv2.LINE_AA)

    print("Number of faces found: {}".format(len(faces)))
    # if (len(faces) > 0):
    #     print('YES')
    # else:
    #     print('NO')
    cv2.imshow('Face Recognition', pic)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:# wait for ESC key to exit
        break
cv2.destroyAllWindows()

    # print("Number of faces found: {}".format(len(faces)))
    # cv2.imshow('Face Recognition', pic)
    # k = cv2.waitKey(0)
    # if k == 27:         # wait for ESC key to exit
    #     cv2.destroyAllWindows()
