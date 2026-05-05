// =============================================================================
// Go — Goroutines, Channels & Concurrency
// =============================================================================
// Topics: goroutines, buffered/unbuffered channels, select, WaitGroup,
//         Mutex, context cancellation, fan-out/fan-in, errgroup.
// Run: go run 07_async.go
// Docs: https://gobyexample.com/goroutines
// =============================================================================
package main

import (
	"context"
	"fmt"
	"sync"
)

// TODO 1: Basic goroutine + WaitGroup
//   var wg sync.WaitGroup
//   for i := 0; i < 5; i++ {
//       wg.Add(1)
//       go func(n int) { defer wg.Done(); time.Sleep(...); fmt.Printf("worker %d\n", n) }(i)
//   }
//   wg.Wait()

// TODO 2: Unbuffered channel — ping/pong
//   ch := make(chan string)
//   Goroutine 1: sends "ping", waits for "pong", repeats 3x
//   Goroutine 2: receives, sends "pong" back, repeats 3x

// TODO 3: Buffered channel as semaphore (limit concurrency)
//   sem := make(chan struct{}, 3)     // max 3 concurrent
//   go func() { sem <- struct{}{}; defer func() { <-sem }(); doWork() }()

// TODO 4: select — timeout pattern
//   select {
//   case result := <-resultCh: ...
//   case <-time.After(2 * time.Second): return errors.New("timeout")
//   }

// TODO 5: Fan-out / fan-in pipeline
//   func generate(nums ...int) <-chan int { ... }
//   func square(in <-chan int) <-chan int { ... }
//   func merge(cs ...<-chan int) <-chan int { ... }  // fan-in using goroutines

// TODO 6: Context cancellation
//   func worker(ctx context.Context, id int) {
//       for { select { case <-ctx.Done(): return; default: doWork() } }
//   }
//   ctx, cancel := context.WithTimeout(context.Background(), time.Second)
//   defer cancel()

// TODO 7: Mutex — safe map
//   type SafeMap struct { mu sync.Mutex; m map[string]int }
//   func (sm *SafeMap) Set(k string, v int) { sm.mu.Lock(); defer sm.mu.Unlock(); sm.m[k]=v }
//   func (sm *SafeMap) Get(k string) (int, bool) { sm.mu.Lock(); defer sm.mu.Unlock(); v,ok:=sm.m[k]; return v,ok }

var _ = context.Background
var _ = sync.Mutex{}

func main() { fmt.Println("Go concurrency — implement TODOs above") }
