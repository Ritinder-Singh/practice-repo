package app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

// @SpringBootApplication is three annotations in one:
//   @EnableAutoConfiguration — Spring Boot auto-configures beans based on your dependencies
//   @ComponentScan          — scans this package and sub-packages for @Service, @Repository, @Controller, etc.
//   @Configuration          — marks this class as a source of bean definitions
@SpringBootApplication
public class Application {

  // Entry point. SpringApplication.run() boots the embedded Tomcat server and wires everything together.
  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }
}