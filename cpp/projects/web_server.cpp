#include <iostream>
#include <string>
#include <sstream>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
// PROJECT: HTTP Web Server | g++ -std=c++20 -o web_server web_server.cpp && ./web_server
//
// TODO 1: TCP listener on port 8080
//   int sock = socket(AF_INET, SOCK_STREAM, 0);
//   // setsockopt SO_REUSEADDR; bind; listen; loop: accept conn
//
// TODO 2: HTTP request parser struct
//   struct Request {
//       std::string method, path, version;
//       std::unordered_map<std::string, std::string> headers;
//       std::string body;
//       static Request parse(const std::string &raw);
//   };
//
// TODO 3: Response builder
//   struct Response {
//       int status = 200;
//       std::string body, content_type = "text/plain";
//       void send(int fd) const;
//   };
//
// TODO 4: Router with std::function handlers
//   using Handler = std::function<Response(const Request&)>;
//   std::unordered_map<std::string, Handler> routes;
//   routes["GET /"]       = [](auto&){ return Response{200, "<h1>Hello</h1>", "text/html"}; };
//   routes["GET /health"] = [](auto&){ return Response{200, R"({"status":"ok"})"}; };
//
// TODO 5: Multithreading with std::thread per connection
//   while (true) {
//       int conn = accept(sock, nullptr, nullptr);
//       std::thread([conn, &router]{ handleConn(conn, router); conn.close(); }).detach();
//   }

int main() {
    std::cout << "Web Server — TODO: implement\n";
    return 0;
}
