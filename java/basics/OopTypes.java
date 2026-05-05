package basics;
// TOPIC: OOP & Type System | javac OopTypes.java && java basics.OopTypes
import java.util.*;

public class OopTypes {
    public static void main(String[] args) {
        // TODO 1: Classes & inheritance — Shape hierarchy
        //   - abstract class Shape {
        //       abstract double area();
        //       abstract double perimeter();
        //       @Override public String toString() { return getClass().getSimpleName() + "[area=" + area() + "]"; }
        //     }
        //   - class Circle extends Shape {
        //       private final double radius;
        //       Circle(double radius) { this.radius = radius; }
        //       @Override double area() { return Math.PI * radius * radius; }
        //       @Override double perimeter() { return 2 * Math.PI * radius; }
        //     }
        //   - class Rectangle extends Shape { ... width, height fields ... }
        //   - Polymorphism: List<Shape> shapes = List.of(new Circle(5), new Rectangle(3,4));
        //     shapes.forEach(System.out::println);

        // TODO 2: Interfaces — Drawable and Resizable
        //   - interface Drawable { void draw(); }
        //   - interface Resizable { void resize(double factor); }
        //   - class Canvas implements Drawable, Resizable {
        //       @Override public void draw() { ... }
        //       @Override public void resize(double factor) { ... }
        //     }
        //   - Demonstrate: Drawable d = new Canvas(); d.draw();  // only Drawable methods visible
        //   - Interface segregation: prefer small, focused interfaces

        // TODO 3: Abstract class vs interface — when to use each
        //   - Abstract class: shared state (fields), constructor logic, partial implementation
        //     abstract class Animal { protected String name; Animal(String n){name=n;} abstract String speak(); }
        //   - Interface: pure contract, multiple inheritance, capabilities across hierarchies
        //     interface Flyable { void fly(); }   interface Swimmable { void swim(); }
        //   - class Duck extends Animal implements Flyable, Swimmable { ... }
        //   - Rule: use interface by default; use abstract class when shared state is needed

        // TODO 4: Generics — Pair and wildcards
        //   - class Pair<A, B> {
        //       private final A first; private final B second;
        //       Pair(A first, B second) { this.first = first; this.second = second; }
        //       A getFirst(); B getSecond(); Pair<B,A> swap() { return new Pair<>(second, first); }
        //       static <X,Y> Pair<X,Y> of(X x, Y y) { return new Pair<>(x, y); }
        //     }
        //   - Bounded wildcards:
        //     double sumList(List<? extends Number> list)  // can read Numbers, not write
        //     void addNumbers(List<? super Integer> list)  // can write Integers
        //   - PECS: Producer Extends, Consumer Super

        // TODO 5: Records (Java 16+)
        //   - record Point(int x, int y) {
        //       // compact constructor for validation:
        //       Point { if (x < 0 || y < 0) throw new IllegalArgumentException("Negative coords"); }
        //       // custom methods are allowed:
        //       double distanceTo(Point other) { return Math.hypot(x - other.x, y - other.y); }
        //       Point translate(int dx, int dy) { return new Point(x + dx, y + dy); }
        //     }
        //   - Records auto-generate: constructor, getters (x(), y()), equals, hashCode, toString
        //   - Records are implicitly final; cannot extend other classes

        // TODO 6: Sealed classes (Java 17+)
        //   - sealed interface Shape permits Circle, Square, Triangle {}
        //   - record Circle(double radius) implements Shape {}
        //   - record Square(double side) implements Shape {}
        //   - record Triangle(double a, double b, double c) implements Shape {}
        //   - Use in exhaustive switch (Java 21):
        //     double area = switch (shape) {
        //         case Circle c    -> Math.PI * c.radius() * c.radius();
        //         case Square s    -> s.side() * s.side();
        //         case Triangle t  -> heronFormula(t.a(), t.b(), t.c());
        //     };  // no default needed — compiler knows all cases

        // TODO 7: Inner classes — four kinds
        //   - Static nested class: OuterClass.StaticNested — no reference to outer; use for helper types
        //     class LinkedList { private static class Node { ... } }
        //   - Inner class: OuterClass.Inner — holds implicit ref to outer; can access outer fields
        //     class Outer { class Inner { void show() { System.out.println(outerField); } } }
        //   - Anonymous class: new Runnable() { @Override public void run() { ... } }
        //     (mostly replaced by lambdas, but still needed for abstract classes with multiple methods)
        //   - Local class: defined inside a method, can access effectively-final local variables
        //   - Prefer static nested over inner unless outer reference is truly needed

        // TODO 8: equals/hashCode contract — Person class
        //   - class Person {
        //       private final String name;
        //       private final int age;
        //       Person(String name, int age) { this.name = name; this.age = age; }
        //       @Override public boolean equals(Object o) {
        //           if (this == o) return true;
        //           if (!(o instanceof Person p)) return false;
        //           return age == p.age && Objects.equals(name, p.name);
        //       }
        //       @Override public int hashCode() { return Objects.hash(name, age); }
        //       @Override public String toString() { return "Person[name=" + name + ", age=" + age + "]"; }
        //     }
        //   - Contract: reflexive, symmetric, transitive, consistent, null returns false
        //   - hashCode contract: equal objects MUST have equal hashCodes
        //   - Test in HashMap and HashSet to verify correct behavior
    }
}
