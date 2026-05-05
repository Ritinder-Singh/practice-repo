<?php
declare(strict_types=1);
// TOPIC: Variables & Types | php 01_variables_types.php
// Docs: https://www.php.net/manual/en/language.types.php

// TODO 1: Basic types — string, int, float, bool, null
//   $str = "hello"; $int = 42; $float = 3.14; $bool = true; $null = null;
//   var_dump($str);       // shows type + value
//   print_r([$str, $int]); // human-readable
//   var_export($float);   // valid PHP syntax representation

// TODO 2: Type juggling — loose (==) vs strict (===) comparison
//   var_dump("0" == false);    // true  — type juggling
//   var_dump("0" === false);   // false — strict type check
//   var_dump(0 == "foo");      // false in PHP 8 (changed from PHP 7!)
//   var_dump("1" == "01");     // true  — numeric string comparison
//   Demonstrate the "spaceship" operator: 1 <=> 2 (returns -1, 0, or 1)

// TODO 3: Type declarations — strict_types=1 enforces them
//   function add(int $a, int $b): int { return $a + $b; }
//   function greet(string $name): string { return "Hello, $name!"; }
//   Union types (PHP 8): function process(int|string $value): void { }
//   Mixed type: function anything(mixed $value): void { }

// TODO 4: Nullable types and null coalescing
//   function findUser(?int $id): ?string { return $id ? "User $id" : null; }
//   $name = findUser(null) ?? "Guest";     // null coalescing
//   $arr['key'] ??= "default";             // null coalescing assignment (PHP 7.4+)

// TODO 5: Named arguments (PHP 8.0)
//   htmlspecialchars(string: "<b>hi</b>", flags: ENT_QUOTES, encoding: "UTF-8");
//   array_slice(array: [1,2,3,4,5], offset: 1, length: 3);
//   Named args can be in any order and you can skip optional params

// TODO 6: Match expression (PHP 8.0) — strict comparison, no fallthrough
//   $status = 404;
//   $text = match($status) {
//       200, 201 => "Success",
//       301, 302 => "Redirect",
//       404      => "Not Found",
//       500      => "Server Error",
//       default  => "Unknown",
//   };

// TODO 7: Enums (PHP 8.1)
//   enum Status: string {
//       case Active   = 'active';
//       case Inactive = 'inactive';
//       case Pending  = 'pending';
//       public function label(): string {
//           return match($this) { self::Active => "Active User", self::Inactive => "Inactive", self::Pending => "Awaiting" };
//       }
//   }
//   echo Status::Active->value;   // "active"
//   echo Status::Active->label(); // "Active User"
//   Status::from("active");       // Status::Active
//   Status::tryFrom("invalid");   // null

// TODO 8: Readonly properties (PHP 8.1) and Intersection types (PHP 8.1)
//   class Point { public function __construct(public readonly float $x, public readonly float $y) {} }
//   $p = new Point(1.0, 2.0); $p->x = 3.0;  // Error: cannot modify readonly
//   Intersection types: function log(Stringable&Countable $item): void { }
