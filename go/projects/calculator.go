// =============================================================================
// PROJECT: Go CLI Calculator
// =============================================================================
// TODO 1 (Mini): REPL — ops: +,-,*,/,%  handle divide-by-zero + bad input
// TODO 2 (Intermediate): Recursive descent parser (no eval)
//   Grammar: expr→term((+|-)term)* | term→factor((*|/)factor)* | factor→NUM|(expr)
// TODO 3 (Advanced): Variables (x:=5+3), built-in funcs (sqrt,abs), history
// Run: go run calculator.go
// =============================================================================
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	fmt.Println("Go Calculator — quit to exit")
	for {
		fmt.Print("> ")
		if !sc.Scan() { break }
		line := strings.TrimSpace(sc.Text())
		if line == "quit" { break }
		// TODO: evaluate and print result
		fmt.Println("(not implemented)")
	}
}
