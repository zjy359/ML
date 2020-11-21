#!/user/
#-*- coding:utf-8 -*-
#!/user/
#-*- coding:utf-8 -*-
import os
import face_recognition
import cv2

boss_names = ['Boss', 'boss']

face_databases_dir = 'face_databases'
user_names = []
user_face_encodings = []

files = os.listdir(face_databases_dir)

for image_shot_name in files:
    user_name,_ = os.path.splitext(image_shot_name)
    user_names.append(user_name)

    image_file_name = os.path.join(face_databases_dir,image_shot_name)
    image_file = face_recognition.load_image_file(image_file_name)
    face_encoding = face_recognition.face_encodings(image_file)[0]
    user_face_encodings.append(face_encoding)


video_capture = cv2.VideoCapture(0)

while True:
    ret,frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame,face_locations)
    names = []
    for face_encoding in face_encodings:
        matchs = face_recognition.compare_faces(user_face_encodings,face_encoding)
        name = "UnKnow"
    for index,is_match in enumerate(matchs):
        if is_match:
            name = user_names[index]
    names.append(name)
    for (top,right,bottom,left),name in zip(face_locations,names):
        color = (0,0,255)
        if name in boss_names:
            color = (0,0,255)
        cv2.rectangle(frame,(left,top),(right,bottom),color,2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name,(left,top-10),font,0.5,color,1)

    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()