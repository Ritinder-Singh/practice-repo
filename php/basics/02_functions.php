<?php
declare(strict_types=1);
// TOPIC: Functions | php 02_functions.php
// Docs: https://www.php.net/manual/en/language.functions.php

// TODO 1: Function signatures with type hints
//   function greet(string $name, string $greeting = "Hello"): string {
//       return "$greeting, $name!";
//   }
//   echo greet("Alice");           // "Hello, Alice!"
//   echo greet("Bob", "Hi");       // "Hi, Bob!"

// TODO 2: Variadic functions
//   function sum(int ...$nums): int { return array_sum($nums); }
//   echo sum(1, 2, 3, 4, 5);  // 15
//   $numbers = [1, 2, 3];
//   echo sum(...$numbers);     // spread operator

// TODO 3: Arrow functions (PHP 7.4) — capture outer scope automatically
//   $multiplier = 3;
//   $fn = fn(int $x) => $x * $multiplier;  // $multiplier captured automatically
//   echo $fn(5);  // 15
//   array_map(fn($x) => $x ** 2, [1,2,3,4]);  // [1,4,9,16]

// TODO 4: First-class callable syntax (PHP 8.1)
//   $fn = strlen(...);         // reference to strlen function
//   $fn = strtoupper(...);
//   array_map(strtoupper(...), ["hello", "world"]);  // ["HELLO", "WORLD"]
//   array_filter($arr, is_numeric(...));

// TODO 5: Closures — manual outer scope capture with use
//   $greeting = "Hello";
//   $greet = function(string $name) use ($greeting): string {
//       return "$greeting, $name!";
//   };
//   // use by reference: use (&$counter)
//   $counter = 0;
//   $increment = function() use (&$counter): void { $counter++; };
//   $increment(); $increment();
//   echo $counter;  // 2

// TODO 6: Generators — lazy sequences with yield
//   function fibonacci(): Generator {
//       [$a, $b] = [0, 1];
//       while (true) {
//           yield $a;
//           [$a, $b] = [$b, $a + $b];
//       }
//   }
//   $fib = fibonacci();
//   foreach (range(0, 9) as $_) { echo $fib->current() . " "; $fib->next(); }
//   // Generator with keys: yield $key => $value

// TODO 7: Memoization using static variable
//   function memoFibonacci(int $n): int {
//       static $cache = [];
//       if ($n <= 1) return $n;
//       return $cache[$n] ??= memoFibonacci($n - 1) + memoFibonacci($n - 2);
//   }

// TODO 8: Higher-order functions
//   array_map(fn($x) => $x * 2, [1,2,3]);          // [2,4,6]
//   array_filter([1,-2,3,-4], fn($x) => $x > 0);   // [1,3]
//   array_reduce([1,2,3,4], fn($carry, $item) => $carry + $item, 0);  // 10
//   usort($arr, fn($a, $b) => $a <=> $b);           // sort ascending
