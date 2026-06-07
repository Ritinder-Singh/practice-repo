package app.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

// @Entity tells JPA this class maps to a database table.
// @Table(name = "users") sets the table name — without it JPA defaults to the class name "user",
// which is a reserved word in SQL and causes issues.
// Lombok's @Getter/@Setter generates all getters and setters at compile time.
// @NoArgsConstructor generates a no-arg constructor, which JPA requires to instantiate entities.
@Entity
@Table(name = "users")
@Getter
@Setter
@NoArgsConstructor
public class User {

  // @Id marks the primary key. @GeneratedValue(IDENTITY) tells the DB to auto-increment it.
  // Use Long (object) not long (primitive) — new entities have a null id before being saved.
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  // @NotBlank is a Bean Validation constraint — rejects null, empty, or whitespace-only strings.
  @NotBlank
  private String name;

  // @Email validates the format. @Column(unique = true) adds a unique constraint in the DB.
  @Email
  @NotBlank
  @Column(unique = true)
  private String email;

  private LocalDateTime createdAt;

  // @PrePersist runs this method automatically just before a new row is inserted.
  // This way createdAt is always set by the app, not manually by the caller.
  @PrePersist
  private void onCreated() {
    createdAt = LocalDateTime.now();
  }
}