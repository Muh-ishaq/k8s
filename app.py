from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket


def get_container_name():
    return os.environ.get("CONTAINER_NAME") or socket.gethostname()


def greet_container(container_name):
    return f"Hello, {escape(container_name)}!"


class GreetingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        greeting = greet_container(get_container_name())
        page = (
            "<!doctype html><html><head><title>Container greeting</title></head>"
            f"<body><h1>{greeting}</h1></body></html>"
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(page.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), GreetingHandler)
    print("Serving at http://localhost:8000")
    server.serve_forever()
