<?php
declare(strict_types=1);
// PROJECT: Async HTTP Client using PHP 8.1 Fibers (Exclusive)
// Fibers are PHP's native coroutines — like goroutines but with manual scheduling.
// Run: php fiber-http-client/AsyncClient.php

// TODO 1: FiberScheduler class — maintains queue of Fiber objects
//   class FiberScheduler {
//       private array $queue = [];
//
//       public function add(Fiber $fiber): void {
//           $this->queue[] = $fiber;
//       }
//
//       public function run(): void {
//           while (!empty($this->queue)) {
//               $next = array_shift($this->queue);
//               if (!$next->isStarted()) {
//                   $next->start();
//               } elseif ($next->isSuspended()) {
//                   $next->resume();
//               }
//               if (!$next->isTerminated() && $next->isSuspended()) {
//                   $this->queue[] = $next;  // re-queue if still running
//               }
//           }
//       }
//   }

// TODO 2: Non-blocking HTTP GET using stream_socket_client with ASYNC flag
//   function httpGet(string $host, string $path): Generator {
//       $socket = stream_socket_client("tcp://$host:80", $errno, $errstr, 30, STREAM_CLIENT_ASYNC_CONNECT);
//       stream_set_blocking($socket, false);
//       fwrite($socket, "GET $path HTTP/1.0\r\nHost: $host\r\nConnection: close\r\n\r\n");
//       $response = "";
//       while (!feof($socket)) {
//           $data = fread($socket, 4096);
//           if ($data === false || $data === "") {
//               yield;  // suspend — give scheduler a chance to run other fibers
//               continue;
//           }
//           $response .= $data;
//       }
//       fclose($socket);
//       return $response;
//   }

// TODO 3: Wrap generator in a Fiber
//   $scheduler = new FiberScheduler();
//   $results = [];
//   $urls = [["httpbin.org", "/get"], ["example.com", "/"], ["httpbin.org", "/ip"]];
//   foreach ($urls as [$host, $path]) {
//       $scheduler->add(new Fiber(function() use ($host, $path, &$results) {
//           $gen = httpGet($host, $path);
//           while ($gen->valid()) { Fiber::suspend(); $gen->next(); }
//           $results[$host . $path] = $gen->getReturn();
//       }));
//   }
//   $scheduler->run();

// TODO 4: Benchmark — compare wall-clock time
//   // Sequential: foreach $urls { curl_exec() } — adds up latencies
//   // Concurrent: FiberScheduler with all requests in parallel — ~= max single latency
//   // Measure: microtime(true) before/after; show speedup

// TODO 5: Timeout support
//   class FiberTimeoutException extends \RuntimeException {}
//   // Track start time per Fiber; if elapsed > $timeout: throw FiberTimeoutException in fiber
//   // Fiber::throw(new FiberTimeoutException("Timed out after {$timeout}s"))
