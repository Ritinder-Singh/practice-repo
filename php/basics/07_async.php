<?php
declare(strict_types=1);
// TOPIC: Fibers & Async | php 07_async.php
// PHP Fibers: https://www.php.net/manual/en/class.fiber.php

// TODO 1: PHP 8.1 Fibers — manual coroutines
//   $fiber = new Fiber(function(): void {
//       $value = Fiber::suspend("first");   // yields "first", receives $value from resume()
//       echo "Got: $value\n";
//       Fiber::suspend("second");
//   });
//   $first = $fiber->start();         // runs until first suspend; returns "first"
//   $second = $fiber->resume("hello"); // resumes with "hello"; returns "second"
//   $fiber->isTerminated();            // true when done

// TODO 2: Fiber scheduler — cooperative multitasking
//   class Scheduler {
//       private array $fibers = [];
//       public function add(Fiber $fiber): void { $this->fibers[] = $fiber; }
//       public function run(): void {
//           while (!empty($this->fibers)) {
//               foreach ($this->fibers as $i => $fiber) {
//                   $fiber->isStarted() ? $fiber->resume() : $fiber->start();
//                   if ($fiber->isTerminated()) unset($this->fibers[$i]);
//               }
//           }
//       }
//   }

// TODO 3: ReactPHP — event loop for non-blocking I/O (external package)
//   // composer require react/event-loop react/http react/socket
//   // $loop = React\EventLoop\Loop::get();
//   // $timer = $loop->addTimer(1.0, fn() => print "1 second passed\n");
//   // $loop->addPeriodicTimer(0.5, fn() => print "tick\n");
//   // $loop->run();

// TODO 4: ReactPHP async HTTP server
//   // $server = new React\Http\HttpServer(function (Psr\Http\Message\ServerRequestInterface $req) {
//   //     return React\Http\Message\Response::plaintext("Hello " . $req->getUri()->getPath());
//   // });
//   // $socket = new React\Socket\SocketServer("0.0.0.0:8080");
//   // $server->listen($socket);
//   // echo "Listening on port 8080\n";
//   // Loop::run();

// TODO 5: pcntl_fork — process-based parallelism (CLI only)
//   // $pid = pcntl_fork();
//   // if ($pid === -1) { throw new RuntimeException("Fork failed"); }
//   // elseif ($pid === 0) { /* child process */ exit(0); }
//   // else { /* parent: wait for child */ pcntl_waitpid($pid, $status); }

// TODO 6: Parallel extension (pecl install parallel)
//   // $runtime = new \parallel\Runtime();
//   // $future  = $runtime->run(function() { return heavyComputation(); });
//   // $result  = $future->value();  // blocks until done

// TODO 7: Amp — another async framework (composer require amphp/amp)
//   // use Amp\async;
//   // $results = Amp\Future\awaitAll([async(fn() => fetchA()), async(fn() => fetchB())]);

// TODO 8: Swoole — coroutine-based server (requires Swoole extension)
//   // Swoole\Coroutine::create(function() {
//   //     $client = new Swoole\Coroutine\Http\Client("httpbin.org", 80);
//   //     $client->get("/get");
//   //     echo $client->body;
//   // });
