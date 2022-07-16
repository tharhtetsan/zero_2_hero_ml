import cv2

cam = cv2.VideoCapture(0)

img_width, img_heith = 400,300

while True:
    rect, frame = cam.read()
    frame = cv2.flip(frame,1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame = cv2.resize(frame,(img_width, img_heith))
    cv2.imshow("test cam",frame)

