# =============================================================================
# PROJECT: Custom Async Web Framework (Exclusive)
# =============================================================================
# Roadmap: Exclusive — custom async framework using asyncio transport/protocol APIs.
# This is how aiohttp/uvicorn work internally.
#
# TODO 1: asyncio.Protocol subclass
#   - data_received(data): buffer until full HTTP request (\r\n\r\n found)
#   - connection_made(transport): store transport reference
#   - connection_lost(exc): cleanup
#
# TODO 2: HTTP request parser
#   - Parse request line: METHOD PATH HTTP/1.1
#   - Parse headers (key: value)
#   - Buffer body per Content-Length
#
# TODO 3: Request / Response objects
#   - Request: method, path, headers, body, query_params (parsed from path)
#   - Response: write status+headers+body through transport
#
# TODO 4: Router
#   - Map (method, path_pattern) → async coroutine handler
#   - Path params: /users/{id} → handler receives {"id": "42"}
#
# TODO 5: Middleware pipeline
#   - Logging middleware (log every request)
#   - Error middleware (catch exceptions → 500 JSON)
#
# TODO 6: asyncio.start_server integration
#   - Create server with Protocol factory via loop.create_server()
#   - Handle backpressure: pause_writing / resume_writing
#
# Run: python framework.py
# Test: curl http://localhost:8080/
# =============================================================================

import asyncio

ROUTES: dict = {}

def route(method: str, path: str):
    def dec(fn): ROUTES[(method.upper(), path)] = fn; return fn
    return dec

class HttpProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self._buffer = b""

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data: bytes):
        self._buffer += data
        if b"\r\n\r\n" in self._buffer:
            asyncio.ensure_future(self._handle())

    async def _handle(self):
        # TODO: parse self._buffer, dispatch to handler, write response
        self.transport.write(b"HTTP/1.1 200 OK\r\nContent-Length: 5\r\n\r\nHello")
        self.transport.close()

    def connection_lost(self, exc):
        pass

async def run():
    loop = asyncio.get_event_loop()
    server = await loop.create_server(HttpProtocol, "127.0.0.1", 8080)
    print("Framework running on http://127.0.0.1:8080")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(run())
