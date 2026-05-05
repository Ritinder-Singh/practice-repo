// =============================================================================
// PROJECT: Concurrent Web Crawler (Exclusive)
// =============================================================================
// TODO 1: Single-threaded BFS crawler — fetch URL, extract <a href> links, recurse
// TODO 2: Worker pool — N goroutines, jobs chan, results chan, WaitGroup
// TODO 3: Context cancellation + rate limiter (golang.org/x/time/rate)
//         Domain scoping, robots.txt respect
// TODO 4: Output — save sitemap.json, print stats (pages, errors, elapsed)
// Run: go run . https://example.com --depth 3 --workers 10
// =============================================================================
package main

import (
	"context"
	"fmt"
	"os"
)

type CrawlResult struct {
	URL string; StatusCode int; Title string; Links []string; Err error
}

// TODO: func fetch(ctx context.Context, url string) CrawlResult
// TODO: func crawl(ctx context.Context, start string, depth, workers int) []CrawlResult

func main() {
	if len(os.Args) < 2 { fmt.Fprintln(os.Stderr, "Usage: ./crawler <url>"); os.Exit(1) }
	ctx := context.Background(); _ = ctx
	fmt.Println("Web crawler — implement TODO sections")
}
