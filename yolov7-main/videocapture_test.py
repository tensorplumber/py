import cv2
cam1 = cv2.VideoCapture(0, apiPreference=None)
print(cam1.isOpened()) #True

while 1:
    ret, frame = cam1.read()

    if not ret:
        break
    cv2.imshow(frame)

