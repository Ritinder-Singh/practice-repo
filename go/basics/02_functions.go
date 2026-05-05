// =============================================================================
// Go — Functions
// =============================================================================
// Topics: multiple return values, named returns, variadic, defer,
//         closures, methods on types, function types as params.
// Run: go run 02_functions.go
// =============================================================================
package main

import "fmt"

// TODO 1: Multiple return values — (result, error) idiom
// func divide(a, b float64) (float64, error) {
//     if b == 0 { return 0, fmt.Errorf("division by zero") }
//     return a / b, nil
// }

// TODO 2: Named return values + naked return
// func minMax(nums []int) (min, max int) {
//     min, max = nums[0], nums[0]
//     for _, n := range nums[1:] {
//         if n < min { min = n }
//         if n > max { max = n }
//     }
//     return  // returns min and max by name
// }

// TODO 3: Variadic functions
// func sum(nums ...int) int { total := 0; for _, n := range nums { total += n }; return total }
// Call: sum(1,2,3)  OR  sum(slice...)  — spread operator

// TODO 4: defer — LIFO order, runs at function exit
// Common patterns: defer f.Close(), defer mu.Unlock(), defer func(){ recover() }()
// Demonstrate: defer inside a loop (pitfall — all defers run at function return, NOT loop iteration)

// TODO 5: Closures
// func makeAdder(x int) func(int) int { return func(y int) int { return x + y } }
// func makeCounter() func() int { n := 0; return func() int { n++; return n } }

// TODO 6: Methods on non-struct types
// type StringSlice []string
// func (ss StringSlice) Contains(s string) bool { ... }
// func (ss StringSlice) Map(fn func(string) string) StringSlice { ... }

// TODO 7: Functions as parameters
// func mapInts(nums []int, fn func(int) int) []int { ... }
// func filter(nums []int, pred func(int) bool) []int { ... }
// func reduce(nums []int, init int, fn func(int, int) int) int { ... }

func main() { fmt.Println("Go functions — implement TODOs above") }
