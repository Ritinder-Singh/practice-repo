// =============================================================================
// Go — Interfaces, Structs & the Type System
// =============================================================================
// Topics: implicit interface implementation, interface composition,
//         type assertions, Stringer, error interface, generics constraints.
// Run: go run 05_oop_or_types.go
// =============================================================================
package main

import (
	"fmt"
	"math"
)

// TODO 1: Implicit interface implementation
//   type Shape interface { Area() float64; Perimeter() float64; String() string }
//   type Circle struct { Radius float64 }
//   func (c Circle) Area() float64 { return math.Pi * c.Radius * c.Radius }
//   No "implements" keyword — Circle satisfies Shape automatically.

// TODO 2: Interface composition
//   type Reader interface { Read(p []byte) (n int, err error) }
//   type Writer interface { Write(p []byte) (n int, err error) }
//   type ReadWriter interface { Reader; Writer }

// TODO 3: Pointer vs value receivers (consistency rule)
//   Use pointer receiver when method modifies state OR type is large.
//   Once any method has pointer receiver, all should for consistency.
//   type Counter struct { n int }
//   func (c *Counter) Inc() { c.n++ }
//   func (c Counter) Value() int { return c.n }

// TODO 4: Custom errors with errors.Is / errors.As
//   type DBError struct { Code int; Message string }
//   func (e *DBError) Error() string { return fmt.Sprintf("[%d] %s", e.Code, e.Message) }
//   Wrap: fmt.Errorf("query failed: %w", err)
//   Check: errors.Is(err, ErrNotFound); var dbErr *DBError; errors.As(err, &dbErr)

// TODO 5: Type assertions and type switches
//   var i interface{} = "hello"
//   s := i.(string)            // panics if wrong type
//   s, ok := i.(string)        // safe form
//   switch v := i.(type) { case string: ... case int: ... }
//   any is alias for interface{} in Go 1.18+

// TODO 6: Generic functions with constraints
//   type Ordered interface { ~int | ~float64 | ~string }
//   func Min[T Ordered](a, b T) T { if a < b { return a }; return b }
//   func Map[T, U any](s []T, fn func(T) U) []U { ... }
//   func Filter[T any](s []T, p func(T) bool) []T { ... }

var _ = math.Pi

func main() { fmt.Println("Go interfaces & types — implement TODOs above") }
