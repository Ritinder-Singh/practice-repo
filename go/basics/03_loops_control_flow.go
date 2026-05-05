// =============================================================================
// Go — Loops & Control Flow
// =============================================================================
// Topics: for (only loop in Go), range, switch, type switch, labeled break.
// Run: go run 03_loops_control_flow.go
// =============================================================================
package main

import "fmt"

func main() {
	// TODO 1: All for forms
	//   for i := 0; i < 10; i++ { }              // C-style
	//   for condition { }                          // while-style
	//   for { break }                              // infinite
	//   for i, v := range slice { }               // range slice
	//   for k, v := range m { }                   // range map
	//   for i, r := range "hello" { }             // range string (runes)
	//   for v := range ch { }                     // range channel

	// TODO 2: switch (no break needed, no fallthrough by default)
	//   switch x { case 1: ... case 2,3: ... default: ... }
	//   switch { case x>0: ... case x<0: ... }    // expressionless switch
	//   fallthrough keyword: explicitly fall to next case

	// TODO 3: Type switch
	//   func describe(i interface{}) string {
	//       switch v := i.(type) {
	//       case int: return fmt.Sprintf("int: %d", v)
	//       case string: return fmt.Sprintf("string: %s", v)
	//       default: return fmt.Sprintf("unknown: %T", v)
	//       }
	//   }

	// TODO 4: Labeled break (break specific loop)
	//   outer: for i := range rows {
	//       for j := range cols {
	//           if condition { break outer }  // exits both loops
	//       }
	//   }

	// TODO 5: FizzBuzz using expressionless switch
	//   for i := 1; i <= 100; i++ {
	//       switch { case i%15==0: ... case i%3==0: ... case i%5==0: ... default: ... }
	//   }

	// TODO 6: Fibonacci — iterative, recursive, closure generator
	//   func fib(n int) int { ... }
	//   func fibGen() func() int { a, b := 0, 1; return func() int { ... } }

	fmt.Println("Go loops & control flow — implement TODOs above")
}
