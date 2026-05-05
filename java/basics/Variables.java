package basics;
// TOPIC: Variables & Types | javac Variables.java && java basics.Variables
// Java docs: https://docs.oracle.com/en/java/index.html
public class Variables {
    public static void main(String[] args) {
        // TODO 1: Primitive types — declare int, long, double, boolean, char
        //   - Print the size in bits of each (Integer.SIZE, Long.SIZE, etc.)
        //   - Print default values by declaring class-level fields and observing them
        //   - Demonstrate int overflow: Integer.MAX_VALUE + 1

        // TODO 2: Wrapper classes — Integer, Double, Boolean
        //   - Boxing: Integer boxed = 42;  Unboxing: int unboxed = boxed;
        //   - Integer.MAX_VALUE, Integer.MIN_VALUE, Integer.toBinaryString(255)
        //   - Integer.parseInt("123"), Double.parseDouble("3.14")
        //   - Demonstrate == vs .equals() trap with cached Integer range (-128 to 127)

        // TODO 3: String operations
        //   - length(), charAt(i), substring(start, end), indexOf("sub"), lastIndexOf
        //   - split(","), trim(), strip() (Java 11+), isBlank()
        //   - String.format("Hello %s, you are %d years old", name, age)
        //   - String.join(", ", "a", "b", "c"), repeat(n) (Java 11+)
        //   - Compare with == vs .equals() vs .equalsIgnoreCase()

        // TODO 4: Type casting
        //   - Widening (implicit): int i = 100; long l = i; double d = l;
        //   - Narrowing (explicit): double d = 9.99; int i = (int) d;  // truncates to 9
        //   - Overflow demo: byte b = (byte) 200;  // wraps to -56
        //   - Char arithmetic: char c = 'A'; int code = c; char next = (char)(c + 1);

        // TODO 5: var keyword (Java 10+) — local type inference
        //   - var list = new ArrayList<String>();  // inferred as ArrayList<String>
        //   - var map = Map.of("key", 42);         // inferred as Map<String, Integer>
        //   - var entry = map.entrySet().iterator().next(); // inferred as Map.Entry
        //   - Note: var is NOT allowed for fields, method params, or return types

        // TODO 6: Constants — static final fields
        //   - static final int MAX_SIZE = 100;          // compile-time constant (inlined by compiler)
        //   - static final String DB_URL = System.getenv("DB_URL");  // runtime constant
        //   - Explain: compile-time constants are substituted at compile time (no class reference needed)
        //   - Use ALL_CAPS naming convention for constants

        // TODO 7: Arrays
        //   - int[] arr = {5, 3, 1, 4, 2};
        //   - Arrays.sort(arr);  System.out.println(Arrays.toString(arr));
        //   - int[][] matrix = new int[3][4];  // 3 rows, 4 cols
        //   - System.arraycopy(src, srcPos, dest, destPos, length)
        //   - Arrays.copyOfRange(arr, 1, 4)  // subarray
        //   - Arrays.fill(arr, 0)            // zero out

        // TODO 8: Enum — Planet enum
        //   - enum Planet { MERCURY(3.303e+23, 2.4397e6), VENUS(...), EARTH(...), MARS(...) }
        //   - Fields: final double mass (kg), final double radius (meters)
        //   - static final double G = 6.67300E-11;
        //   - Method: double surfaceGravity() { return G * mass / (radius * radius); }
        //   - Method: double surfaceWeight(double otherMass) { return otherMass * surfaceGravity(); }
        //   - In main: print weight on each planet for an 80kg person
    }
}
