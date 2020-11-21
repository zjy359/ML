#!/user/
#-*- coding:utf-8 -*-

import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret,frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    for top,right,bottom,left in face_locations:
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,225),2)

    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()