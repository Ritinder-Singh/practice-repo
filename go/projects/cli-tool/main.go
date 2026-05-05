// =============================================================================
// PROJECT: Go CLI Tool (Major) — cobra + viper
// =============================================================================
// TODO 1: Setup — go get github.com/spf13/cobra github.com/spf13/viper
// TODO 2: Subcommands
//   fetch <url>         — HTTP GET, pretty-print response
//   config set k v      — write to ~/.cli-config.yaml via viper
//   config get k        — read from config
//   version             — print version
// TODO 3: Global flags — --output json|table|plain  --timeout 30s  --verbose
// Run: go run ./
// =============================================================================
package main

import (
	"fmt"
	"os"
)

func main() {
	// TODO: cobra root command + Execute()
	fmt.Fprintln(os.Stderr, "CLI — implement cobra commands in cmd/")
	os.Exit(1)
}
