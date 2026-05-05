// =============================================================================
// WebSocket — Server & Client Patterns
// =============================================================================
// Topics: ws server setup, connection lifecycle, broadcasting, rooms,
//         heartbeat/ping-pong, reconnect logic, typed message protocol.
// Run: npx ts-node 09_websocket.ts
// Ref: Resume — "WebSocket" (Technical Skills)
// =============================================================================

// npm install ws @types/ws

// =============================================================================
// 1. TYPED MESSAGE PROTOCOL
// =============================================================================

type MessageType =
  | "join_room"
  | "leave_room"
  | "chat"
  | "broadcast"
  | "ping"
  | "pong"
  | "error";

interface WSMessage {
  type: MessageType;
  payload: unknown;
  roomId?: string;
  clientId?: string;
  timestamp: number;
}

function createMessage(type: MessageType, payload: unknown, roomId?: string): WSMessage {
  return { type, payload, roomId, timestamp: Date.now() };
}


// =============================================================================
// 2. SERVER — ROOM-BASED BROADCAST
// =============================================================================

/*
import { WebSocket, WebSocketServer } from "ws";

interface Client {
  id: string;
  ws: WebSocket;
  rooms: Set<string>;
  lastPing: number;
}

class RoomServer {
  private wss: WebSocketServer;
  private clients = new Map<string, Client>();
  private rooms = new Map<string, Set<string>>(); // roomId → Set<clientId>

  constructor(port: number) {
    this.wss = new WebSocketServer({ port });
    this.wss.on("connection", this.handleConnection.bind(this));
    this.startHeartbeat();
    console.log(`WebSocket server on ws://localhost:${port}`);
  }

  private handleConnection(ws: WebSocket) {
    const clientId = crypto.randomUUID();
    const client: Client = { id: clientId, ws, rooms: new Set(), lastPing: Date.now() };
    this.clients.set(clientId, client);

    ws.send(JSON.stringify(createMessage("broadcast", { clientId }, undefined)));

    ws.on("message", (raw) => {
      try {
        const msg: WSMessage = JSON.parse(raw.toString());
        this.handleMessage(clientId, msg);
      } catch {
        ws.send(JSON.stringify(createMessage("error", "Invalid JSON")));
      }
    });

    ws.on("close", () => this.removeClient(clientId));
    ws.on("pong", () => { client.lastPing = Date.now(); });
  }

  private handleMessage(clientId: string, msg: WSMessage) {
    switch (msg.type) {
      case "join_room":
        this.joinRoom(clientId, msg.roomId!);
        break;
      case "leave_room":
        this.leaveRoom(clientId, msg.roomId!);
        break;
      case "chat":
        this.broadcastToRoom(msg.roomId!, { ...msg, clientId }, clientId);
        break;
      case "ping":
        this.clients.get(clientId)?.ws.send(JSON.stringify(createMessage("pong", {})));
        break;
    }
  }

  private joinRoom(clientId: string, roomId: string) {
    const client = this.clients.get(clientId)!;
    client.rooms.add(roomId);
    if (!this.rooms.has(roomId)) this.rooms.set(roomId, new Set());
    this.rooms.get(roomId)!.add(clientId);
    this.broadcastToRoom(roomId, createMessage("broadcast", `${clientId} joined`), clientId);
  }

  private leaveRoom(clientId: string, roomId: string) {
    this.clients.get(clientId)?.rooms.delete(roomId);
    this.rooms.get(roomId)?.delete(clientId);
  }

  private broadcastToRoom(roomId: string, msg: WSMessage, excludeId?: string) {
    const memberIds = this.rooms.get(roomId) ?? new Set();
    for (const memberId of memberIds) {
      if (memberId === excludeId) continue;
      const member = this.clients.get(memberId);
      if (member?.ws.readyState === WebSocket.OPEN) {
        member.ws.send(JSON.stringify(msg));
      }
    }
  }

  private removeClient(clientId: string) {
    const client = this.clients.get(clientId);
    if (!client) return;
    for (const roomId of client.rooms) {
      this.rooms.get(roomId)?.delete(clientId);
    }
    this.clients.delete(clientId);
  }

  // Heartbeat: detect dead connections
  private startHeartbeat(intervalMs = 30_000) {
    setInterval(() => {
      const now = Date.now();
      for (const [id, client] of this.clients) {
        if (now - client.lastPing > intervalMs * 2) {
          client.ws.terminate();
          this.clients.delete(id);
        } else {
          client.ws.ping();
        }
      }
    }, intervalMs);
  }
}
*/


// =============================================================================
// 3. CLIENT — AUTO-RECONNECT
// =============================================================================

/*
class ReconnectingWSClient {
  private ws: WebSocket | null = null;
  private reconnectDelay = 1000;
  private maxDelay = 30_000;
  private handlers = new Map<MessageType, (msg: WSMessage) => void>();

  constructor(private url: string) {
    this.connect();
  }

  private connect() {
    this.ws = new WebSocket(this.url);

    this.ws.onopen = () => {
      console.log("Connected");
      this.reconnectDelay = 1000; // reset on success
    };

    this.ws.onmessage = ({ data }) => {
      const msg: WSMessage = JSON.parse(data);
      this.handlers.get(msg.type)?.(msg);
    };

    this.ws.onclose = () => {
      console.log(`Disconnected. Reconnecting in ${this.reconnectDelay}ms...`);
      setTimeout(() => this.connect(), this.reconnectDelay);
      this.reconnectDelay = Math.min(this.reconnectDelay * 2, this.maxDelay);
    };

    this.ws.onerror = (err) => console.error("WS error:", err);
  }

  on(type: MessageType, handler: (msg: WSMessage) => void) {
    this.handlers.set(type, handler);
    return this;
  }

  send(msg: WSMessage) {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(msg));
    }
  }

  joinRoom(roomId: string) {
    this.send(createMessage("join_room", {}, roomId));
  }

  chat(roomId: string, text: string) {
    this.send(createMessage("chat", { text }, roomId));
  }
}
*/


// =============================================================================
// 4. WEBSOCKET IN EXPRESS/FASTAPI (upgrade pattern)
// =============================================================================

/*
// Express HTTP → WS upgrade on same port:
import http from "http";
import express from "express";
import { WebSocketServer } from "ws";

const app = express();
const server = http.createServer(app);
const wss = new WebSocketServer({ server, path: "/ws" });

wss.on("connection", (ws) => {
  ws.on("message", (msg) => {
    ws.send(`Echo: ${msg}`);
  });
});

server.listen(3000);
// Clients connect to: ws://localhost:3000/ws
*/


// =============================================================================
// 5. COMMON PATTERNS CHEATSHEET
// =============================================================================

const WS_PATTERNS = {
  readyStates: {
    CONNECTING: 0,
    OPEN: 1,
    CLOSING: 2,
    CLOSED: 3,
  },

  // Always check readyState before sending
  safeSend: "if (ws.readyState === WebSocket.OPEN) ws.send(data)",

  // Binary data (audio streams, file transfer)
  binaryMode: "ws.binaryType = 'arraybuffer'; ws.send(new Uint8Array(buffer))",

  // Ping-pong keepalive (server side)
  heartbeat: "ws.ping(); ws.on('pong', () => client.isAlive = true)",

  // Broadcast to all connected clients
  broadcast: "wss.clients.forEach(client => { if (client.readyState === WS.OPEN) client.send(data) })",

  // URL params for auth (token in query string)
  authOnUpgrade: "const token = new URL(req.url, 'http://x').searchParams.get('token')",
} as const;


// =============================================================================
// DEMO (runnable without ws package)
// =============================================================================

console.log("=== WebSocket Typed Message Protocol ===");
const msg = createMessage("chat", { text: "Hello room!" }, "room-123");
console.log(JSON.stringify(msg, null, 2));

console.log("\n=== Ready State Reference ===");
console.log(WS_PATTERNS.readyStates);

console.log("\n=== Common Patterns ===");
Object.entries(WS_PATTERNS).forEach(([key, val]) => {
  if (typeof val === "string") console.log(`  ${key}: ${val}`);
});

// TODO: Implement RoomServer and test with wscat (npm i -g wscat)
// TODO: Add authentication middleware on the upgrade event
// TODO: Add rate limiting per client (sliding window on message count)
