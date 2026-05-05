# =============================================================================
# PROJECT: Python Web Server (raw sockets only)
# =============================================================================
# TODO 1 (Mini): Single-threaded server on localhost:8080
#   - Parse GET/POST requests from raw bytes
#   - Route: GET / → HTML, GET /time → JSON, POST /echo → echo body
#   - Proper HTTP/1.1 response format with headers
#
# TODO 2 (Intermediate): Multi-threaded + router decorator
#   @route("GET", "/")  decorator pattern
#   Serve static files from ./public/ with MIME type detection
#   ThreadPoolExecutor for connection handling
#
# TODO 3 (Advanced): Keep-alive + logging
#   Connection: keep-alive support (loop reading on same socket)
#   Request logging: [timestamp] METHOD /path STATUS elapsed_ms
#   Graceful shutdown on SIGTERM (signal module)
#
# Run: python web_server.py
# Test: curl http://localhost:8080/
# =============================================================================

import socket, threading, json
from datetime import datetime

HOST, PORT = "127.0.0.1", 8080
ROUTES = {}

def route(method, path):
    def dec(fn): ROUTES[(method.upper(), path)] = fn; return fn
    return dec

# TODO: implement parse_request(raw: bytes) -> dict
# TODO: implement make_response(status: int, body: str, ctype: str = "text/html") -> bytes
# TODO: implement handle_client(conn, addr)
# TODO: implement run_server()

@route("GET", "/")
def index(req):
    return 200, "<h1>Hello from Python!</h1>", "text/html"

@route("GET", "/time")
def get_time(req):
    return 200, json.dumps({"time": datetime.now().isoformat()}), "application/json"

if __name__ == "__main__":
    print("Implement parse_request, make_response, handle_client, run_server")
    # run_server()
