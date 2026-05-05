// =============================================================================
// Web Crawler — Worker Pool
// =============================================================================
package main

import (
	"context"
	"fmt"
	"sync"
)

// TODO: func startWorkers(ctx context.Context, jobs <-chan string, results chan<- CrawlResult, n int)
//   - Launch n goroutines, each reading from jobs, writing to results
//   - WaitGroup to know when all done; close(results) when finished

var _ = context.Background; var _ = sync.WaitGroup{}; var _ = fmt.Println
