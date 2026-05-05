package app.repository;

// PROJECT: Spring Boot User Repository
//
// TODO 1: Extend JpaRepository<User, Long>
//   public interface UserRepository extends JpaRepository<User, Long> { ... }
//
// TODO 2: Add custom query methods (Spring Data JPA generates SQL automatically):
//   Optional<User> findByEmail(String email);
//   boolean existsByEmail(String email);
//   List<User> findByNameContainingIgnoreCase(String name);
//
// TODO 3: Add a @Query example:
//   @Query("SELECT u FROM User u WHERE u.createdAt > :since")
//   List<User> findRecentUsers(@Param("since") LocalDateTime since);

public interface UserRepository {
    // stub — extend JpaRepository<User, Long> once Spring Boot is set up
}
