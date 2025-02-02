import http.server
import socketserver

PORT = 8080  # Change the port to 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<!DOCTYPE html>')
        self.wfile.write(b'<html lang="en">')
        self.wfile.write(b'<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>My Pure Python Website</title></head>')
        self.wfile.write(b'<body>')
        self.wfile.write(b'<h1>Welcome to My Python Website</h1>')
        self.wfile.write(b'<p>This website was created using only Python (no HTML files needed!)</p>')
        self.wfile.write(b'</body>')
        self.wfile.write(b'</html>')

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
d