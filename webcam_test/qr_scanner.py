import glob
import cv2
import pandas as pd
import pathlib

def read_qr_code():
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """
    cap = cv2.VideoCapture(1)

    
    try:
        # img = cv2.imread(filename)........................
        detect = cv2.QRCodeDetector()
        ret, frame = cap.read()

        value, points, straight_qrcode = detect.detectAndDecode(frame)
        return value
    except:
        return

read_qr_code()




# value = read_qr_code('data/00003090-PHOTO-2022-03-19-08-31-34.jpg')
# print(value)

# df = pd.DataFrame(columns=['filename', 'qr'])
# files = glob.glob('data/*.jpg')

# for file in files:

#     qr = read_qr_code(file)
#     row = {'filename': file, 'qr': qr}
    
#     df = df.append(row, ignore_index=True)

# df.head()