import cv2
from datetime import datetime

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("test", frame)
        keyValue = cv2.waitKey(1) & 0xFF
        if keyValue == ord('q'):
            break
        elif keyValue == ''.join(str(ord(c)) for c in 'not yet\n'):
            fn = "{}.jpg".format(datetime.now().strftime("%Y-%m-%d_%H%M%S"))
            # fn = "test.jpg"
            cv2.imwrite(fn, frame)

cap.release()
cv2.destroyAllWindows()