// =============================================================================
// Go — Variables & Types
// =============================================================================
// Topics: var vs :=, zero values, type conversion, constants, iota,
//         type definitions vs aliases, string internals (bytes vs runes).
// Run: go run 01_variables_types.go
// Docs: https://go.dev/tour/basics/1
// =============================================================================
package main

import "fmt"

func main() {
	// TODO 1: var vs := declaration
	//   var x int = 42           // explicit type
	//   y := 3.14                // short declaration (inferred float64)
	//   var s string             // zero value: ""
	//   var b bool               // zero value: false
	//   Zero values: int→0, float64→0.0, bool→false, string→"", pointer→nil

	// TODO 2: Multiple assignment and blank identifier
	//   x, y := 1, 2
	//   x, y = y, x              // swap without temp variable
	//   _, err := someFunc()     // discard first return value

	// TODO 3: Constants and iota
	//   const Pi = 3.14159
	//   type Weekday int
	//   const ( Sun Weekday = iota; Mon; Tue; Wed; Thu; Fri; Sat )
	//   iota with expressions: 1 << iota (bit flags), iota*100, etc.
	//   Implement String() method on Weekday to print day names.

	// TODO 4: Type definitions vs aliases
	//   type Celsius float64       // new named type — NOT assignable to float64 without conversion
	//   type Alias = float64       // alias — same as float64, interchangeable
	//   func (c Celsius) ToFahrenheit() float64 { return float64(c)*9/5 + 32 }

	// TODO 5: Basic numeric types
	//   int, int8, int16, int32, int64
	//   uint, uint8, uint16, uint32, uint64
	//   float32, float64, complex64, complex128
	//   byte (= uint8), rune (= int32 — Unicode code point)
	//   import "unsafe"; fmt.Println(unsafe.Sizeof(int64(0)))  → 8

	// TODO 6: String internals
	//   Strings are immutable byte slices (UTF-8 encoded).
	//   len("Hello") = 5 (bytes), len("世界") = 6 (bytes but 2 chars)
	//   for i, r := range "Hello, 世界" { fmt.Printf("%d: %c\n", i, r) }
	//   Convert: []byte(s), []rune(s), string([]byte{...})

	fmt.Println("Go variables & types — implement TODOs above")
}
