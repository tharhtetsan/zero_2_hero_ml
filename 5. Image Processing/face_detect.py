import cv2

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img_width, img_heith = 400,300

while True:
    rect, frame = cam.read()
    frame = cv2.flip(frame,1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
    frame = cv2.resize(frame,(img_width, img_heith))
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Red Channel",frame)
    