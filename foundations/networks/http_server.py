# =============================================================================
# Networks — HTTP/1.1 Server from Raw Sockets
# =============================================================================
# Build a minimal HTTP/1.1 server using ONLY Python's socket + threading modules.
# No frameworks (no Flask, no http.server). Teaches TCP, request parsing, responses.
#
# Run: python http_server.py
# Test: curl http://localhost:8080/  |  curl http://localhost:8080/time
# Docs: https://www.rfc-editor.org/rfc/rfc7230
# =============================================================================

import socket
import threading
from datetime import datetime

HOST, PORT = "127.0.0.1", 8080

STATUS_MESSAGES = {200: "OK", 201: "Created", 400: "Bad Request",
                   404: "Not Found", 405: "Method Not Allowed", 500: "Internal Server Error"}

# =============================================================================
# TODO 1: Parse raw HTTP request bytes into a dict
# =============================================================================
# HTTP request format:
#   GET /path HTTP/1.1\r\n
#   Header-Name: value\r\n
#   \r\n
#   [optional body]
#
# Return dict: { "method": str, "path": str, "version": str,
#                "headers": dict[str,str], "body": bytes }
#
# def parse_request(raw: bytes) -> dict:
#     header_section, _, body = raw.partition(b"\r\n\r\n")
#     lines = header_section.decode().split("\r\n")
#     method, path, version = lines[0].split(" ")
#     headers = {}
#     for line in lines[1:]:
#         if ": " in line:
#             k, v = line.split(": ", 1)
#             headers[k.lower()] = v
#     return {"method": method, "path": path, "version": version,
#             "headers": headers, "body": body}

# =============================================================================
# TODO 2: Build HTTP response bytes
# =============================================================================
# HTTP response format:
#   HTTP/1.1 200 OK\r\n
#   Content-Type: text/html\r\n
#   Content-Length: 13\r\n
#   \r\n
#   Hello, World!
#
# def make_response(status: int, body: str, content_type: str = "text/html") -> bytes:
#     body_bytes = body.encode()
#     status_line = f"HTTP/1.1 {status} {STATUS_MESSAGES.get(status, 'Unknown')}"
#     headers = "\r\n".join([
#         f"Content-Type: {content_type}; charset=utf-8",
#         f"Content-Length: {len(body_bytes)}",
#         f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}",
#         "Connection: close",
#     ])
#     return f"{status_line}\r\n{headers}\r\n\r\n".encode() + body_bytes

# =============================================================================
# TODO 3: Router — map (method, path) to handler functions
# =============================================================================
# ROUTES: dict[tuple[str, str], Callable] = {}
#
# def route(method: str, path: str):
#     def decorator(fn):
#         ROUTES[(method.upper(), path)] = fn
#         return fn
#     return decorator
#
# @route("GET", "/")
# def index(req): return 200, "<h1>Hello from raw sockets!</h1>", "text/html"
#
# @route("GET", "/time")
# def get_time(req): return 200, datetime.now().isoformat(), "text/plain"
#
# @route("POST", "/echo")
# def echo(req): return 200, req["body"].decode(errors="replace"), "text/plain"

# =============================================================================
# TODO 4: Handle a single client connection
# =============================================================================
# def handle_client(conn: socket.socket, addr: tuple) -> None:
#     try:
#         raw = conn.recv(8192)
#         if not raw:
#             return
#         req = parse_request(raw)
#         handler = ROUTES.get((req["method"], req["path"]))
#         if handler is None:
#             response = make_response(404, "<h1>404 Not Found</h1>")
#         else:
#             status, body, ctype = handler(req)
#             response = make_response(status, body, ctype)
#         conn.sendall(response)
#     except Exception as e:
#         conn.sendall(make_response(500, f"Error: {e}"))
#     finally:
#         conn.close()

# =============================================================================
# TODO 5: Main server loop — accept connections, spawn threads
# =============================================================================
# def run_server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
#         server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         server.bind((HOST, PORT))
#         server.listen(5)
#         print(f"Server at http://{HOST}:{PORT}")
#         while True:
#             conn, addr = server.accept()
#             t = threading.Thread(target=handle_client, args=(conn, addr))
#             t.daemon = True
#             t.start()

# =============================================================================
# TODO 6: Extensions
# =============================================================================
# 6a: Serve static files from ./public/ with correct MIME types
# 6b: URL path parameters: /users/<id> → handler receives id
# 6c: Keep-Alive — loop reading multiple requests on same connection
# 6d: Chunked transfer encoding for streaming responses

if __name__ == "__main__":
    print("Implement TODOs above, then call run_server()")
    # run_server()
