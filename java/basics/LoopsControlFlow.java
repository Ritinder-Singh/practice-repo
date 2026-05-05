package basics;
// TOPIC: Loops & Control Flow | javac LoopsControlFlow.java && java basics.LoopsControlFlow
import java.util.*;
import java.util.stream.*;

public class LoopsControlFlow {
    public static void main(String[] args) {
        // TODO 1: for, while, do-while — FizzBuzz 1-100
        //   - for loop:    standard i=1; i<=100; i++
        //   - while loop:  int i = 1; while (i <= 100) { ... i++; }
        //   - do-while:    int i = 1; do { ... i++; } while (i <= 100);
        //   - Logic: divisible by 15 → "FizzBuzz", by 3 → "Fizz", by 5 → "Buzz", else number

        // TODO 2: Enhanced for-each — iterate List and Map
        //   - List<String> fruits = List.of("apple", "banana", "cherry");
        //     for (String fruit : fruits) { System.out.println(fruit); }
        //   - Map<String, Integer> scores = Map.of("Alice", 95, "Bob", 87);
        //     for (Map.Entry<String, Integer> entry : scores.entrySet()) { ... }
        //   - Also iterate using Map.forEach((k, v) -> ...)

        // TODO 3: break with label — nested loops
        //   - outer: for (int i = 0; i < 5; i++) {
        //       for (int j = 0; j < 5; j++) {
        //           if (i == 2 && j == 3) break outer;
        //           System.out.println(i + "," + j);
        //       }
        //   }
        //   - Also demonstrate continue with label to skip to next outer iteration

        // TODO 4: switch expression (Java 14+) — arrow syntax
        //   - String dayType = switch (dayOfWeek) {
        //       case MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY -> "WEEKDAY";
        //       case SATURDAY, SUNDAY -> "WEEKEND";
        //     };
        //   - Also show switch expression with yield for multi-line cases
        //   - Compare with old switch statement syntax

        // TODO 5: Pattern matching instanceof (Java 16+)
        //   - Object obj = "Hello, World!";
        //     if (obj instanceof String s) { System.out.println(s.length()); }
        //   - Use in a method that accepts Object and handles String, Integer, List differently
        //   - Combine with && guard: if (obj instanceof String s && s.length() > 5) { ... }

        // TODO 6: Stream pipeline
        //   - List<Integer> numbers = List.of(1, 2, 3, ..., 20);
        //   - Find all even numbers, square them, sort descending, collect to list
        //     numbers.stream().filter(n -> n % 2 == 0).map(n -> n * n)
        //            .sorted(Comparator.reverseOrder()).collect(Collectors.toList())
        //   - Also: IntStream.rangeClosed(1, 100).sum()
        //   - reduce: numbers.stream().reduce(0, Integer::sum)

        // TODO 7: Iterator vs ListIterator — safe removal during traversal
        //   - Iterator<String> it = list.iterator();
        //     while (it.hasNext()) { if (condition) it.remove(); }  // safe
        //   - ListIterator<String> lit = list.listIterator();
        //     lit.hasPrevious(), lit.previousIndex(), lit.set(...), lit.add(...)
        //   - Show why for-each + list.remove() throws ConcurrentModificationException

        // TODO 8: Optional — chaining to avoid NPE
        //   - Optional<String> opt = Optional.ofNullable(getValue());
        //   - opt.map(String::toUpperCase).orElse("DEFAULT")
        //   - opt.flatMap(s -> Optional.ofNullable(s.isEmpty() ? null : s))
        //   - opt.ifPresent(System.out::println)
        //   - opt.filter(s -> s.length() > 3).orElseThrow(() -> new RuntimeException("Too short"))
        //   - Note: never do opt.get() without isPresent() check; prefer orElse/orElseThrow
    }
}
