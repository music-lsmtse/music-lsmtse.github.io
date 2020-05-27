"""Set up a server

do `python server.py`
then access http://localhost:8000/msa_demo/index.html
"""
import os
os.chdir('../')
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
