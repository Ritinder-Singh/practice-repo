<?php
declare(strict_types=1);
// TOPIC: Advanced PHP | php 08_advanced.php

// TODO 1: Reflection API — inspect classes at runtime
//   $rc = new ReflectionClass(User::class);
//   $rc->getMethods(ReflectionMethod::IS_PUBLIC);
//   $rc->getProperties();
//   $method = $rc->getMethod('getName');
//   $method->invoke(new User("Alice"));
//   $rc->getAttributes();  // get PHP 8 attributes

// TODO 2: Attributes (PHP 8.0) — structured metadata
//   #[Attribute(Attribute::TARGET_CLASS | Attribute::TARGET_METHOD)]
//   class Route {
//       public function __construct(public readonly string $path, public readonly string $method = "GET") {}
//   }
//   #[Route("/users", "GET")]
//   class UserController {
//       #[Route("/users/{id}", "GET")]
//       public function show(int $id): void { }
//   }
//   // Read with Reflection:
//   $attrs = (new ReflectionClass(UserController::class))->getAttributes(Route::class);
//   $route = $attrs[0]->newInstance();  // Route{path: "/users", method: "GET"}

// TODO 3: Magic methods — complete reference
//   __construct, __destruct     // lifecycle
//   __get, __set, __isset, __unset  // property access
//   __call, __callStatic        // method calls
//   __toString, __debugInfo     // string conversion / var_dump output
//   __clone                     // object cloning
//   __serialize, __unserialize  // custom serialization (PHP 7.4+)
//   __invoke                    // call object as function

// TODO 4: SPL (Standard PHP Library) — underused but powerful
//   SplStack, SplQueue, SplMinHeap, SplMaxHeap, SplDoublyLinkedList
//   SplFixedArray — fixed-size, faster than array for numeric indices
//   SplObjectStorage — map from objects to values
//   ArrayObject — array with OOP interface + sorting, flagging
//   RecursiveIteratorIterator + RecursiveDirectoryIterator — walk directories

// TODO 5: Generators — advanced patterns
//   function pipeline(iterable $source, callable ...$pipes): \Generator {
//       foreach ($source as $value) {
//           foreach ($pipes as $pipe) { $value = $pipe($value); }
//           yield $value;
//       }
//   }
//   // Generator delegation with yield from:
//   function outer(): \Generator { yield 1; yield from inner(); yield 4; }
//   function inner(): \Generator { yield 2; yield 3; }
//   iterator_to_array(outer());  // [1, 2, 3, 4]

// TODO 6: WeakReference and WeakMap — avoid memory leaks in caches
//   $obj = new stdClass();
//   $ref = WeakReference::create($obj);
//   $ref->get();    // returns $obj
//   unset($obj);
//   $ref->get();    // returns null — object was garbage collected
//   // WeakMap: keys are objects, removed automatically when object is collected

// TODO 7: Match expression with no-match error
//   $result = match($value) { 1 => "one", 2 => "two" };
//   // throws UnhandledMatchError if no case matches (unlike switch which falls through to nothing)

// TODO 8: JIT (Just-In-Time compilation) — PHP 8.0+
//   // Enable in php.ini: opcache.enable=1, opcache.jit_buffer_size=128M, opcache.jit=tracing
//   // JIT helps CPU-bound code (image processing, math), not I/O-bound
//   // opcache_get_status()['jit'] to check status
