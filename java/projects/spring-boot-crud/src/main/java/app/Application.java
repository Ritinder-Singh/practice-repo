package app;

// TODO: Add these annotations once Spring Boot is set up:
// @SpringBootApplication
// public class Application { public static void main(String[] args) { SpringApplication.run(Application.class, args); } }

// public class Application {
//    public static void main(String[] args) {
//        System.out.println("TODO: bootstrap Spring Boot app");
//      }
//}

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }
}
