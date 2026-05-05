// =============================================================================
// Go — Arrays, Slices, Maps, Structs
// =============================================================================
// Topics: slice internals (ptr/len/cap), slice tricks, map operations,
//         struct embedding, JSON tags, generics (Go 1.18+).
// Run: go run 04_data_structures.go
// Docs: https://go.dev/blog/slices-intro
// =============================================================================
package main

import "fmt"

func main() {
	// TODO 1: Array vs slice
	//   arr := [5]int{1,2,3,4,5}     // fixed size, value type
	//   sli := []int{1,2,3,4,5}      // dynamic, reference type
	//   make([]int, len, cap)         // pre-allocate
	//   Show: copy(), append() may reallocate if cap exceeded

	// TODO 2: Slice tricks
	//   Delete index i (order preserved): s = append(s[:i], s[i+1:]...)
	//   Delete index i (order irrelevant): s[i]=s[len(s)-1]; s=s[:len(s)-1]
	//   Insert at index i: s = append(s[:i+1], s[i:]...); s[i] = val
	//   Reverse in-place: for i,j := 0,len(s)-1; i<j; i,j = i+1,j-1 { s[i],s[j]=s[j],s[i] }
	//   Deduplicate: sort + unique filter, or map-based

	// TODO 3: Maps
	//   m := make(map[string]int)
	//   m["key"] = 42
	//   v, ok := m["key"]      // ok=false if missing
	//   delete(m, "key")
	//   Iterate: for k,v := range m { }  (order NOT guaranteed)
	//   PITFALL: var m map[string]int — nil map, assigning panics!

	// TODO 4: Struct embedding
	//   type Address struct { Street, City, Country string }
	//   type Person struct { Name string; Address }  // embedded
	//   p.City  // promoted field — direct access
	//   Method promotion: methods of embedded type available on outer type

	// TODO 5: JSON marshaling with struct tags
	//   type Product struct {
	//       ID    int     `json:"id"`
	//       Name  string  `json:"name"`
	//       Price float64 `json:"price,omitempty"`
	//   }
	//   import "encoding/json"
	//   data, _ := json.Marshal(p); json.Unmarshal(data, &p)

	// TODO 6: Generic Stack using Go 1.18+ generics
	//   type Stack[T any] struct { items []T }
	//   func (s *Stack[T]) Push(item T) { s.items = append(s.items, item) }
	//   func (s *Stack[T]) Pop() (T, bool) { ... }

	fmt.Println("Go data structures — implement TODOs above")
}
