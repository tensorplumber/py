import http.server
import socketserver
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == 27: # use ESC to .............quit
        break

cap.release()
cv2.destroyAllWindows()
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(pageData, "utf8"))
        elif self.path.startswith('/image'):
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()

            ret, frame = cap.read()
            _, jpg = cv2.imencode(".jpg", frame)

            self.wfile.write(jpg)
        else:
            self.send_response(404)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port ", PORT)
    try:
        httpd.serve_forever()
    except:
        pass