// =============================================================================
// PROJECT: TypeScript HTTP Server (Node.js only, no Express)
// =============================================================================
// TODO 1 (Mini): http.createServer — GET /, GET /api/time, POST /echo
// TODO 2 (Intermediate): Mini-router + middleware chain
//   type Middleware = (req:IncomingMessage, res:ServerResponse, next:()=>void) => void
//   app.use(logger); app.get("/path", handler); app.post("/path", handler)
// TODO 3 (Advanced): WebSocket upgrade — implement handshake + frame parser
//   Real-time chat: broadcast messages to all connected clients
//
// Run: npx ts-node web_server.ts
// =============================================================================

import http from "http";

const PORT = 8080;
const ROUTES = new Map<string, (req: http.IncomingMessage, res: http.ServerResponse) => void>();

function get(path: string, handler: typeof ROUTES extends Map<string, infer V> ? V : never) {
  ROUTES.set(`GET:${path}`, handler);
}

// TODO: implement request body parsing
// TODO: implement middleware chain (use, next)

get("/", (req, res) => {
  res.writeHead(200, { "Content-Type": "text/html" });
  res.end("<h1>Hello from TypeScript!</h1>");
});

const server = http.createServer((req, res) => {
  const handler = ROUTES.get(`${req.method}:${req.url}`);
  if (handler) handler(req, res);
  else { res.writeHead(404); res.end("Not Found"); }
});

server.listen(PORT, () => console.log(`http://localhost:${PORT}`));
