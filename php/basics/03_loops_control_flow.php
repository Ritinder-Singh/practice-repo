<?php
declare(strict_types=1);
// TOPIC: Loops & Control Flow | php 03_loops_control_flow.php

// TODO 1: for, while, do-while — FizzBuzz 1-100
//   for ($i = 1; $i <= 100; $i++) {
//       echo match(0) {
//           $i % 15 => "FizzBuzz",
//           $i % 3  => "Fizz",
//           $i % 5  => "Buzz",
//           default => $i,
//       } . "\n";
//   }

// TODO 2: foreach — arrays and objects
//   $fruits = ["apple" => 1, "banana" => 2, "cherry" => 3];
//   foreach ($fruits as $name => $count) { echo "$name: $count\n"; }
//   // Modify by reference: foreach ($arr as &$val) { $val *= 2; } unset($val);

// TODO 3: list() / [] destructuring
//   [$first, $second, ...$rest] = [1, 2, 3, 4, 5];
//   ["name" => $name, "age" => $age] = ["name" => "Alice", "age" => 30];
//   // Nested: [[$a, $b], [$c, $d]] = [[1, 2], [3, 4]];
//   // In foreach: foreach ($points as [$x, $y]) { }

// TODO 4: match expression — strict comparison, no fallthrough, returns value
//   $value = "2";
//   $result = match(true) {
//       $value > 100   => "large",
//       $value > 50    => "medium",
//       $value > 0     => "small",
//       default        => "non-positive",
//   };

// TODO 5: break with numeric argument — break outer loop
//   for ($i = 0; $i < 3; $i++) {
//       for ($j = 0; $j < 3; $j++) {
//           if ($j === 1) break 2;  // break both loops
//       }
//   }

// TODO 6: continue with numeric argument
//   for ($i = 0; $i < 5; $i++) {
//       for ($j = 0; $j < 5; $j++) {
//           if ($j === 2) continue 2;  // skip to next outer iteration
//       }
//   }

// TODO 7: Generator-based loops — memory-efficient iteration
//   function csvLines(string $filename): Generator {
//       $fh = fopen($filename, 'r');
//       while (!feof($fh)) { yield fgetcsv($fh); }
//       fclose($fh);
//   }
//   // foreach (csvLines("data.csv") as $row) { process($row); }

// TODO 8: Recursive iteration — directory tree walker
//   function walkDir(string $dir): Generator {
//       $items = new DirectoryIterator($dir);
//       foreach ($items as $item) {
//           if ($item->isDot()) continue;
//           yield $item->getPathname();
//           if ($item->isDir()) yield from walkDir($item->getPathname());
//       }
//   }
//   // yield from delegates to another generator
