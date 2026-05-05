// =============================================================================
// Go — Error Handling
// =============================================================================
// Topics: error interface, sentinel errors, wrapping (%w), errors.Is/As,
//         panic/recover, custom error types, multi-error accumulation.
// Run: go run 06_error_handling.go
// =============================================================================
package main

import (
	"errors"
	"fmt"
)

// TODO 1: Basic error handling — check immediately, add context
//   result, err := op()
//   if err != nil { return fmt.Errorf("context message: %w", err) }
//   Write: readConfig(path string) (map[string]string, error)

// TODO 2: Sentinel errors
//   var ErrNotFound = errors.New("not found")
//   var ErrPermission = errors.New("permission denied")
//   Callers: if errors.Is(err, ErrNotFound) { handle 404 }

// TODO 3: Custom error types
//   type HTTPError struct { StatusCode int; Body string }
//   func (e *HTTPError) Error() string { ... }
//   errors.As usage: var httpErr *HTTPError; if errors.As(err, &httpErr) { ... }

// TODO 4: Error wrapping chain
//   Low level:   return fmt.Errorf("db query: %w", sqlErr)
//   Mid level:   return fmt.Errorf("get user: %w", dbErr)
//   Top level:   if errors.Is(err, sql.ErrNoRows) { return ErrNotFound }

// TODO 5: panic and recover
//   func safeDo(fn func()) (err error) {
//       defer func() {
//           if r := recover(); r != nil {
//               err = fmt.Errorf("panic: %v", r)
//           }
//       }()
//       fn()
//       return nil
//   }

// TODO 6: Collect multiple errors
//   type MultiError struct { Errors []error }
//   func (m *MultiError) Error() string { ... }
//   func (m *MultiError) Add(err error) { m.Errors = append(m.Errors, err) }
//   func (m *MultiError) Err() error { if len(m.Errors)==0 { return nil }; return m }

var _ = errors.New

func main() { fmt.Println("Go error handling — implement TODOs above") }
