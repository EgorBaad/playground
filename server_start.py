from http.server import HTTPServer, CGIHTTPRequestHandler
from main import __main__
server_address = ("127.0.0.1", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print("Server is up and running at 127.0.0.1:8000")
httpd.serve_forever()