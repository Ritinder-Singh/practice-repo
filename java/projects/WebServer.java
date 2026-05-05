package projects;
// PROJECT: Raw Java HTTP Server (no frameworks) | javac WebServer.java && java projects.WebServer
// Build a multi-threaded HTTP/1.1 server using only java.net.ServerSocket

import java.io.*;
import java.net.*;

public class WebServer {

    // TODO 1: Create ServerSocket on port 8080
    //   - new ServerSocket(8080)
    //   - Set SO_REUSEADDR to avoid "Address already in use" on restart

    // TODO 2: Accept connections in a loop
    //   - Socket client = serverSocket.accept();
    //   - Handle each connection in a new Thread (or use ExecutorService pool)

    // TODO 3: Parse HTTP request
    //   - Read first line: "GET /path HTTP/1.1"
    //   - Read headers until blank line "\r\n"
    //   - Store in HashMap<String, String>

    // TODO 4: Router — map paths to handlers
    //   - GET / → 200 "Hello from Java HTTP Server"
    //   - GET /time → 200 with current timestamp (LocalDateTime.now())
    //   - GET /health → 200 {"status":"ok"} with Content-Type: application/json
    //   - else → 404 Not Found

    // TODO 5: Send HTTP/1.1 response
    //   - "HTTP/1.1 200 OK\r\n"
    //   - "Content-Type: text/plain\r\n"
    //   - "Content-Length: N\r\n"
    //   - "Connection: close\r\n"
    //   - "\r\n"
    //   - body

    // TODO 6: Thread pool — use Executors.newFixedThreadPool(10) instead of new Thread per request

    // TODO 7: Graceful shutdown — Runtime.getRuntime().addShutdownHook(new Thread(() -> serverSocket.close()))

    public static void main(String[] args) throws Exception {
        System.out.println("TODO: implement HTTP server on port 8080");
    }
}
