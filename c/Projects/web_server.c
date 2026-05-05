#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
// PROJECT: HTTP/1.1 Web Server | gcc -o web_server web_server.c && ./web_server
//
// TODO 1: TCP listener on port 8080
//   int sock = socket(AF_INET, SOCK_STREAM, 0);
//   setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &1, sizeof(1));
//   struct sockaddr_in addr = { .sin_family=AF_INET, .sin_port=htons(8080),
//                               .sin_addr.s_addr=INADDR_ANY };
//   bind(sock, (struct sockaddr*)&addr, sizeof(addr));
//   listen(sock, SOMAXCONN);
//   int conn = accept(sock, NULL, NULL);
//
// TODO 2: HTTP request parsing
//   - Read bytes into buffer: recv(conn, buf, sizeof(buf)-1, 0)
//   - Parse request line: sscanf(buf, "%s %s %s", method, path, version)
//   - Find headers after first "\r\n"; body after "\r\n\r\n"
//
// TODO 3: Router — match path → handler
//   if (strcmp(path, "/") == 0)       serve_index(conn);
//   else if (strcmp(path, "/health")) serve_health(conn);
//   else                              serve_404(conn);
//
// TODO 4: Response builder
//   void respond(int conn, int status, const char *body) {
//       char hdr[512];
//       snprintf(hdr, sizeof(hdr),
//           "HTTP/1.1 %d OK\r\nContent-Length: %zu\r\nConnection: close\r\n\r\n",
//           status, strlen(body));
//       send(conn, hdr, strlen(hdr), 0);
//       send(conn, body, strlen(body), 0);
//   }
//
// TODO 5: Concurrent connections using fork() or pthreads
//   // fork: each accept spawns child process to handle connection
//   // pthread: spawn thread per connection

int main(void) {
    printf("Web Server — TODO: implement\n");
    return 0;
}
