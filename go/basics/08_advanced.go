// =============================================================================
// Go — Advanced Topics
// =============================================================================
// Topics: reflection, generics constraints, embed, sync/atomic, build tags, pprof.
// Run: go run 08_advanced.go
// =============================================================================
package main

import (
	"fmt"
	"reflect"
)

// TODO 1: Reflection
//   reflect.TypeOf(v), reflect.ValueOf(v)
//   Implement: func prettyPrint(v interface{}) — iterates struct fields via reflection
//   Implement: func setField(obj interface{}, name string, val interface{}) error

// TODO 2: Generic constraints
//   type Number interface { ~int | ~int32 | ~int64 | ~float32 | ~float64 }
//   func Sum[T Number](s []T) T { ... }
//   func Contains[T comparable](s []T, v T) bool { ... }
//   type Set[T comparable] struct { items map[T]struct{} }

// TODO 3: embed package
//   //go:embed static/
//   var staticFS embed.FS
//   Serve embedded files via http.FileServer(http.FS(staticFS))

// TODO 4: sync/atomic — lock-free counter vs mutex counter (benchmark)
//   type AtomicCounter struct { n int64 }
//   func (c *AtomicCounter) Inc() { atomic.AddInt64(&c.n, 1) }
//   func (c *AtomicCounter) Load() int64 { return atomic.LoadInt64(&c.n) }

// TODO 5: Build tags
//   // //go:build linux
//   Create: platform_linux.go, platform_darwin.go, platform_windows.go
//   Each implements: func PlatformName() string

// TODO 6: runtime/pprof basics
//   import "runtime/pprof"
//   f, _ := os.Create("cpu.prof")
//   pprof.StartCPUProfile(f); defer pprof.StopCPUProfile()
//   Run: go tool pprof cpu.prof

var _ = reflect.TypeOf

func main() { fmt.Println("Go advanced topics — implement TODOs above") }
