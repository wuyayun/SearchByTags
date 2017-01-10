import os
from http.server import HTTPServer, CGIHTTPRequestHandler

workdir = '.'
os.chdir(workdir)

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi']

host = ''
port = 80

server = HTTPServer((host, port), handler)
server.serve_forever()
