<?php
declare(strict_types=1);
// TOPIC: Data Structures | php 04_data_structures.php

// TODO 1: Array as ordered list — push/pop, shift/unshift, slice, splice
//   $arr = [1, 2, 3];
//   array_push($arr, 4, 5);    // or $arr[] = 4;
//   array_pop($arr);           // removes and returns last
//   array_shift($arr);         // removes and returns first
//   array_unshift($arr, 0);    // prepends
//   array_slice($arr, 1, 3);   // non-destructive slice
//   array_splice($arr, 1, 2, ["a", "b"]);  // destructive replace

// TODO 2: Array as hash map (associative array)
//   $map = ["alice" => 30, "bob" => 25];
//   array_key_exists("alice", $map);   // true
//   isset($map["charlie"]);            // false
//   array_merge($map, ["carol" => 28]);
//   ksort($map); arsort($map);         // sort by key / by value descending

// TODO 3: SPL data structures — typed, memory-efficient
//   $stack  = new SplStack();  $stack->push(1); $stack->top(); $stack->pop();
//   $queue  = new SplQueue();  $queue->enqueue(1); $queue->dequeue();
//   $minHeap = new SplMinHeap(); $minHeap->insert(3); $minHeap->insert(1); $minHeap->top();
//   $maxHeap = new SplMaxHeap();
//   $pq = new SplPriorityQueue(); $pq->insert("low", 1); $pq->insert("high", 10);

// TODO 4: Array functions — must-know
//   array_map(fn($x) => $x * 2, $arr);
//   array_filter($arr, fn($x) => $x > 0);
//   array_reduce($arr, fn($carry, $item) => $carry + $item, 0);
//   array_unique([1,1,2,2,3]);
//   array_flip(["a" => 1, "b" => 2]);   // swap keys and values
//   array_combine(["a","b"], [1,2]);     // keys array + values array → associative

// TODO 5: Sorting
//   sort($arr);           // ascending, reindex
//   rsort($arr);          // descending, reindex
//   asort($arr);          // ascending, preserve keys
//   krsort($arr);         // descending by key
//   usort($arr, fn($a, $b) => $a <=> $b);
//   uasort($arr, fn($a, $b) => strlen($a) <=> strlen($b));  // preserve keys

// TODO 6: Implement Stack using array
//   class Stack {
//       private array $items = [];
//       public function push(mixed $item): void { $this->items[] = $item; }
//       public function pop(): mixed { return array_pop($this->items); }
//       public function peek(): mixed { return end($this->items); }
//       public function isEmpty(): bool { return empty($this->items); }
//   }

// TODO 7: Implement Queue using two stacks (amortized O(1))
//   class Queue {
//       private array $inbox = [];
//       private array $outbox = [];
//       public function enqueue(mixed $item): void { $this->inbox[] = $item; }
//       public function dequeue(): mixed {
//           if (empty($this->outbox)) { $this->outbox = array_reverse($this->inbox); $this->inbox = []; }
//           return array_pop($this->outbox);
//       }
//   }

// TODO 8: WeakMap (PHP 8.0) — keys are objects, held weakly (no GC prevention)
//   $weakMap = new WeakMap();
//   $obj = new stdClass();
//   $weakMap[$obj] = "metadata";
//   unset($obj);  // $obj removed from WeakMap automatically
