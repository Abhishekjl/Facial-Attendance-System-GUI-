import cv2
import numpy as np
import face_recognition
imgpooja = face_recognition.load_image_file('images/Poojahegde.jpg')
imgpooja = cv2.cvtColor(imgpooja,cv2.COLOR_BGR2RGB)

# to find the face location 
face = face_recognition.face_locations(imgpooja)[0]
# convert image into encoding 
train_encode = face_recognition.face_encodings(imgpooja)[0]

# lets test an image
test = face_recognition.load_image_file('images/1.jpg')
test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
test_encode = face_recognition.face_encodings(test)[0]

print(face_recognition.compare_faces([train_encode],test_encode))


# cv2.rectangle(imgpooja, (face[3], face[0]),(face[1], face[2]), (255,0,255), 1)
# cv2.imshow('Pooja', imgpooja)
# cv2.waitKey(0)