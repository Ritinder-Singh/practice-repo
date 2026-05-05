// =============================================================================
// PROJECT: Go Web Server
// =============================================================================
// TODO 1 (Mini): net/http — GET /, GET /time (JSON), POST /echo
//   requestLogger middleware: log METHOD /path STATUS elapsed
// TODO 2 (Intermediate): chi router + middleware chain
//   go get github.com/go-chi/chi/v5
//   Route groups, path params /users/{id}, CORS, recovery middleware
// TODO 3 (Advanced): sqlx + Postgres CRUD + graceful shutdown
//   go get github.com/jmoiron/sqlx github.com/lib/pq
//   http.Server.Shutdown() on SIGTERM
// Run: go run web_server.go
// =============================================================================
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

func logger(next http.Handler) http.Handler {
	// TODO: log each request with timing
	return next
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "<h1>Hello from Go!</h1>")
	})
	mux.HandleFunc("/time", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(map[string]string{"time": time.Now().Format(time.RFC3339)})
	})
	fmt.Println("http://localhost:8080")
	http.ListenAndServe(":8080", logger(mux))
}
