package basics;
// TOPIC: Methods & Functional Interfaces | javac Functions.java && java basics.Functions
import java.util.*;
import java.util.function.*;

public class Functions {
    public static void main(String[] args) {
        // TODO 1: Method overloading — write 3 versions of add()
        //   - int    add(int a, int b)
        //   - double add(double a, double b)
        //   - String add(String a, String b)   // concatenation
        //   - Call all three and print results; note compiler picks version by argument types

        // TODO 2: Varargs — sum any number of ints
        //   - int sum(int... nums)  { int total = 0; for (int n : nums) total += n; return total; }
        //   - Call: sum(), sum(1), sum(1,2,3), sum(new int[]{4,5,6})
        //   - Note: varargs must be last parameter; internally it's an array

        // TODO 3: Recursion with memoization
        //   - long fibonacci(int n, Map<Integer,Long> memo)
        //     Base: n <= 1 → return n; Check memo first; store result before returning
        //   - long factorial(int n, Map<Integer,Long> memo)
        //     Base: n <= 1 → return 1; Check memo first
        //   - Print fibonacci(0..15) and factorial(0..12)

        // TODO 4: Lambda expressions
        //   - Comparator<String> byLength = (a, b) -> Integer.compare(a.length(), b.length());
        //   - Runnable r = () -> System.out.println("Running!");
        //   - Supplier<String> greeting = () -> "Hello, World!";
        //   - Consumer<String> printer = s -> System.out.println(s);
        //   - Predicate<Integer> isEven = n -> n % 2 == 0;
        //   - Sort a List<String> using byLength comparator

        // TODO 5: Method references — four kinds
        //   - Static:    Integer::parseInt          (Function<String, Integer>)
        //   - Instance (unbound): String::toUpperCase (Function<String, String>)
        //   - Instance (bound):   "hello"::contains  (Predicate<String>)
        //   - Constructor:        ArrayList::new      (Supplier<ArrayList>)
        //   - Demonstrate each by passing to stream operations or functional interfaces

        // TODO 6: Custom @FunctionalInterface
        //   - @FunctionalInterface interface Transformer<T, R> { R transform(T input); }
        //   - Use it: Transformer<String, Integer> strLen = String::length;
        //   - Transformer<Integer, String> intStr = i -> "Number: " + i;
        //   - Chain: apply strLen then intStr to "Hello"

        // TODO 7: Default & static interface methods
        //   - interface Greeter {
        //       String name();                              // abstract
        //       default String greet() { return "Hello, " + name() + "!"; }
        //       static Greeter of(String name) { return () -> name; }
        //     }
        //   - Implement anonymously and via lambda; demonstrate default method override

        // TODO 8: Generic methods
        //   - <T extends Comparable<T>> T max(T a, T b) { return a.compareTo(b) >= 0 ? a : b; }
        //   - <T> List<T> repeat(T item, int times)    { ... }
        //   - <K,V> Map<V,K> invertMap(Map<K,V> map)   { ... }
        //   - Call each with Integer, String, and custom Comparable class
    }
}
