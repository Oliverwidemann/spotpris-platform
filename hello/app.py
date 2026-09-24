import os, time, json
from http.server import BaseHTTPRequestHandler, HTTPServer
import signal, sys

signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))
START = time.time()
POD = os.environ.get("POD_NAME", "ukendt")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"pod": POD, "uptime_s": round(time.time() - START)})
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode() + b"\n")

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()