import cgi
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class TodoHandler(BaseHTTPRequestHandler):
    TODOS=[]

    def do_GET(self):
        if self.path!='/':
            self.send_error(404, "File not found!")
            return

        msg=json.dump(self.TODOS)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(msg)

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if ctype == 'application/json':
            length = int(self.headers['content-length'])
            post_values = json.loads(self.rfile.read(length))
            self.TODOS.append(post_values)
        else:
            self.send_error(415, "Only json data is supported.")
            return
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(post_values)

if __name__ =='__main__':
    server=HTTPServer(('127.0.0.1',8080), TodoHandler)
    print("Server starting!")
    server.serve_forever()