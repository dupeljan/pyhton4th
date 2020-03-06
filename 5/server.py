from http.server import HTTPServer as s 
from http.server import CGIHTTPRequestHandler as rh
server_adress = ("",8000)
h = s(server_adress,rh)
h.serve_forever()