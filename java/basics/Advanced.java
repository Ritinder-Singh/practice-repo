package basics;
// TOPIC: Advanced Java | javac Advanced.java && java basics.Advanced
import java.lang.reflect.*;
import java.lang.annotation.*;
import java.time.*;
import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Advanced {
    public static void main(String[] args) {
        // TODO 1: Reflection — runtime class inspection
        //   - Class<?> clazz = Class.forName("java.util.ArrayList");
        //   - clazz.getMethods()          — all public methods (including inherited)
        //   - clazz.getDeclaredMethods()  — all methods declared in this class
        //   - Method m = clazz.getMethod("size");  m.invoke(instance);
        //   - Field f = clazz.getDeclaredField("size");  f.setAccessible(true);  f.get(instance);
        //   - Constructor<?> c = clazz.getDeclaredConstructor(); Object obj = c.newInstance();
        //   - Use case: build a simple dependency injection container using @Inject annotation

        // TODO 2: Custom annotations
        //   - @Retention(RetentionPolicy.RUNTIME)
        //     @Target(ElementType.FIELD)
        //     public @interface Validate {
        //         int min() default 0;
        //         int max() default Integer.MAX_VALUE;
        //         String message() default "Validation failed";
        //     }
        //   - Apply: class User { @Validate(min=2, max=50) String name; @Validate(min=18) int age; }
        //   - Process: scan fields with reflection, check @Validate, enforce constraints
        //   - Retention policies: SOURCE (erased at compile), CLASS (in bytecode), RUNTIME (accessible via reflection)

        // TODO 3: Stream advanced collectors
        //   - flatMap: Stream<List<Integer>> → Stream<Integer>
        //     listOfLists.stream().flatMap(Collection::stream).collect(toList())
        //   - groupingBy: Map<String, List<Person>> byCity = people.stream()
        //       .collect(Collectors.groupingBy(Person::getCity));
        //   - groupingBy with downstream: Map<String, Long> countByCity =
        //       people.stream().collect(Collectors.groupingBy(Person::getCity, Collectors.counting()));
        //   - partitioningBy: Map<Boolean, List<Integer>> evenOdd =
        //       numbers.stream().collect(Collectors.partitioningBy(n -> n % 2 == 0));
        //   - toMap: Map<String, Integer> nameLengths =
        //       names.stream().collect(Collectors.toMap(s -> s, String::length, (a,b) -> a));

        // TODO 4: String operations — performance and formatting
        //   - String concatenation in loop — DON'T: "result" += s  (creates O(n^2) garbage)
        //   - StringBuilder sb = new StringBuilder(); sb.append(...); sb.toString()  — O(n) total
        //   - StringJoiner sj = new StringJoiner(", ", "[", "]"); sj.add("a"); sj.toString() → "[a]"
        //   - String.join(", ", list)  — shorthand using StringJoiner internally
        //   - String.format("%-10s %5d", name, value)  — left-align, right-align with width
        //   - "Hello %s".formatted("World")  — Java 15+ instance method, equivalent to String.format
        //   - Benchmark 10,000 concatenations: String vs StringBuilder, print time diff

        // TODO 5: Date/Time API (java.time — Java 8+)
        //   - LocalDate today = LocalDate.now();  today.plusDays(30);  today.getYear();
        //   - LocalTime now = LocalTime.now();    now.getHour();  now.withMinute(0);
        //   - LocalDateTime dt = LocalDateTime.of(2024, Month.JANUARY, 1, 12, 0);
        //   - ZonedDateTime zdt = ZonedDateTime.now(ZoneId.of("America/New_York"));
        //   - Duration d = Duration.between(start, end);  d.toMinutes();
        //   - Period p = Period.between(birthDate, today);  p.getYears();
        //   - DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        //     dt.format(fmt);  LocalDateTime.parse("2024-01-01 12:00", fmt);

        // TODO 6: Serialization
        //   - class Employee implements Serializable {
        //       private static final long serialVersionUID = 1L;
        //       private String name;
        //       private double salary;
        //       private transient String passwordHash;  // NOT serialized
        //     }
        //   - Write: ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("emp.ser"));
        //     oos.writeObject(employee);
        //   - Read:  ObjectInputStream ois = new ObjectInputStream(new FileInputStream("emp.ser"));
        //     Employee e = (Employee) ois.readObject();
        //   - Custom: override writeObject/readObject for encryption or transformation
        //   - Warning: serialVersionUID mismatch causes InvalidClassException

        // TODO 7: Module system (Java 9+ JPMS)
        //   - Create module-info.java in src root:
        //     module com.myapp.core {
        //         requires java.logging;        // depends on java.logging module
        //         requires transitive java.sql;  // re-exports to dependents
        //         exports com.myapp.api;         // makes package visible to other modules
        //         exports com.myapp.internal to com.myapp.tests;  // qualified export
        //         opens com.myapp.model;         // allows deep reflection (e.g., for frameworks)
        //         uses com.myapp.spi.Plugin;     // declares ServiceLoader usage
        //         provides com.myapp.spi.Plugin with com.myapp.impl.DefaultPlugin;
        //     }
        //   - Compile: javac --module-source-path src -d out $(find src -name "*.java")
        //   - Run: java --module-path out -m com.myapp.core/com.myapp.Main
        //   - Benefits: strong encapsulation, reliable configuration, reduced attack surface

        // TODO 8: GC tuning — garbage collector options
        //   - G1GC (default Java 9+): balanced throughput/latency, region-based, good for heap > 4GB
        //     -XX:+UseG1GC -XX:MaxGCPauseMillis=200
        //   - ZGC (Java 15+ production): ultra-low latency (<1ms pauses), scalable to TB heaps
        //     -XX:+UseZGC -XX:ZCollectionInterval=5
        //   - Shenandoah (Red Hat, Java 12+): concurrent compaction, similar goals to ZGC
        //     -XX:+UseShenandoahGC
        //   - ParallelGC: max throughput, higher pauses — good for batch jobs
        //     -XX:+UseParallelGC -XX:GCTimeRatio=19
        //   - Key flags: -Xms512m (initial heap), -Xmx4g (max heap), -Xss512k (stack per thread)
        //   - GC logging: -Xlog:gc*:file=gc.log:time,level
        //   - Tools: jstat -gcutil <pid> 1000, VisualVM, JFR (Java Flight Recorder)
    }
}
