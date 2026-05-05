<?php
declare(strict_types=1);
// TOPIC: OOP & Type System | php 05_oop_or_types.php
// Docs: https://www.php.net/manual/en/language.oop5.php

// TODO 1: Classes — constructor promotion, readonly, constants
//   class User {
//       public function __construct(
//           public readonly int $id,
//           public string $name,
//           private string $password,
//           public readonly \DateTimeImmutable $createdAt = new \DateTimeImmutable(),
//       ) {}
//       public function setName(string $name): static { $this->name = $name; return $this; }
//   }

// TODO 2: Interfaces — multiple implementation
//   interface Serializable { public function toJson(): string; }
//   interface Validatable { public function validate(): bool; }
//   class FormData implements Serializable, Validatable { ... }

// TODO 3: Abstract classes
//   abstract class Shape {
//       abstract public function area(): float;
//       public function describe(): string { return get_class($this) . " with area " . $this->area(); }
//   }
//   class Circle extends Shape {
//       public function __construct(private float $radius) {}
//       public function area(): float { return M_PI * $this->radius ** 2; }
//   }

// TODO 4: Traits — reuse behavior without inheritance
//   trait Timestampable {
//       private ?\DateTimeImmutable $createdAt = null;
//       private ?\DateTimeImmutable $updatedAt = null;
//       public function touch(): void { $this->updatedAt = new \DateTimeImmutable(); }
//   }
//   class Post { use Timestampable; }
//   // Trait conflict resolution: use A, B { A::method insteadof B; B::method as aliasMethod; }

// TODO 5: Final classes and methods
//   final class Singleton {
//       private static ?self $instance = null;
//       private function __construct() {}
//       public static function getInstance(): static {
//           return self::$instance ??= new static();
//       }
//   }

// TODO 6: Magic methods — __toString, __get, __set, __call, __invoke
//   class MagicClass {
//       private array $data = [];
//       public function __get(string $name): mixed { return $this->data[$name] ?? null; }
//       public function __set(string $name, mixed $value): void { $this->data[$name] = $value; }
//       public function __isset(string $name): bool { return isset($this->data[$name]); }
//       public function __invoke(string $arg): string { return "Called with $arg"; }
//       public function __toString(): string { return json_encode($this->data); }
//   }

// TODO 7: Fibers (PHP 8.1) in class context (see 07_async.php for full example)
//   // Briefly: Fiber is a primitive for manual coroutines

// TODO 8: Intersection types and never return type (PHP 8.1)
//   function process(Countable&Stringable $input): void { echo count($input) . ": " . $input; }
//   function throwError(string $msg): never { throw new \RuntimeException($msg); }
//   // never means function never returns (always throws or exits)
