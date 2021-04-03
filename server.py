from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		print("GET")
		self.send_response(200)
		self.send_handler('Content-type', 'text/html')
		self.end_handlers()
		self.wfile.write(b'Hello world')

	def do_POST(self):
		print("POST")
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		response = BytesIO()
		response.write(b'This is POST request. ')
		response.write(b'Received: ')
		response.write(body)
		self.wfile.write(response.getvalue())

httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
