package app.repository;

import app.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

// Extending JpaRepository<User, Long> gives you free CRUD methods with no implementation needed:
//   save(), findById(), findAll(), deleteById(), existsById(), count(), etc.
// The two type params are: the entity class, and the type of its primary key.
// Spring creates the actual implementation at runtime — you never write it.
public interface UserRepository extends JpaRepository<User, Long> {

  // Derived queries — Spring reads the method name and generates the SQL automatically.
  // "findBy" + field name = WHERE clause. No SQL or implementation needed.
  Optional<User> findByEmail(String email);

  boolean existsByEmail(String email);

  // "Containing" = SQL LIKE %name%. "IgnoreCase" = case-insensitive match.
  List<User> findByNameContainingIgnoreCase(String name);

  // When the method name gets too complex, write JPQL (Java-flavored SQL) directly with @Query.
  // "User" here refers to the Java class, not the table name.
  // @Param binds the method parameter to the :since placeholder in the query.
  @Query("SELECT u FROM User u WHERE u.createdAt > :since")
  List<User> findRecentUsers(@Param("since") LocalDateTime since);
}