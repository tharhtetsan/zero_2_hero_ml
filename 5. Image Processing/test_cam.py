import cv2

cam = cv2.VideoCapture(0)

img_width, img_heith = 400,300

while True:
    rect, frame = cam.read()
    frame = cv2.flip(frame,1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
    frame = cv2.resize(frame,(img_width, img_heith))


    blue_channel = frame.copy()
    # set green and red channels to 0
    blue_channel[:, :, 1] = 0
    blue_channel[:, :, 2] = 0


    green_channel = frame.copy()
    # set blue and red channels to 0
    green_channel[:, :, 0] = 0
    green_channel[:, :, 2] = 0

    red_channel = frame.copy()
    # set blue and green channels to 0
    red_channel[:, :, 0] = 0
    red_channel[:, :, 1] = 0
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    cv2.imshow("Black and White",gray_image)
    cv2.imshow("Original Camera input",frame)
    cv2.imshow("Blue Channel",blue_channel)
    cv2.imshow("Green Channel",green_channel)
    cv2.imshow("Red Channel",red_channel)
    