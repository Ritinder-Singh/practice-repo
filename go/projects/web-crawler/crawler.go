// =============================================================================
// Web Crawler — HTML parsing + BFS logic
// =============================================================================
package main

import (
	"fmt"
	"net/http"
	"net/url"
)

// TODO: func extractLinks(body []byte, base *url.URL) []string — parse <a href>
// TODO: func bfsCrawl(ctx context.Context, start string, maxDepth int) []CrawlResult

var _ = http.Get; var _ = url.Parse; var _ = fmt.Println
