package basics;
// TOPIC: Error Handling | javac ErrorHandling.java && java basics.ErrorHandling
import java.io.*;
import java.util.logging.*;

public class ErrorHandling {
    public static void main(String[] args) {
        // TODO 1: try-catch-finally — exception hierarchy
        //   - FileNotFoundException extends IOException extends Exception
        //   - Catch more specific FIRST, then broader:
        //     try { new FileInputStream("missing.txt"); }
        //     catch (FileNotFoundException e) { System.out.println("File not found: " + e.getMessage()); }
        //     catch (IOException e)            { System.out.println("IO error: " + e.getMessage()); }
        //     finally                          { System.out.println("Always runs"); }
        //   - finally runs even if return or exception occurs in catch

        // TODO 2: Multi-catch — single catch block for unrelated exceptions
        //   - try {
        //       String s = null;
        //       int[] arr = Integer.parseInt(s) > 0 ? new int[5] : null;
        //       arr[0] = 1;
        //     } catch (NumberFormatException | NullPointerException | ArrayIndexOutOfBoundsException e) {
        //       System.out.println("Caught: " + e.getClass().getSimpleName() + " — " + e.getMessage());
        //     }
        //   - Note: variables caught in multi-catch are implicitly final

        // TODO 3: try-with-resources — AutoCloseable
        //   - try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
        //       String line; while ((line = reader.readLine()) != null) System.out.println(line);
        //     }  // reader.close() called automatically even if exception thrown
        //   - Multiple resources (closed in reverse order):
        //     try (InputStream in = ...; OutputStream out = ...) { ... }
        //   - Implement AutoCloseable: class Resource implements AutoCloseable { @Override public void close() { ... } }

        // TODO 4: Custom exceptions — checked vs unchecked
        //   - Checked (extends Exception) — caller MUST handle or declare:
        //     class InsufficientFundsException extends Exception {
        //         private final double amount;
        //         InsufficientFundsException(double amount) {
        //             super("Insufficient funds: need " + amount + " more");
        //             this.amount = amount;
        //         }
        //         double getAmount() { return amount; }
        //     }
        //   - Unchecked (extends RuntimeException) — no forced handling:
        //     class InvalidUserException extends RuntimeException {
        //         InvalidUserException(String userId) { super("User not found: " + userId); }
        //     }
        //   - Rule: use checked for recoverable conditions; unchecked for programming errors

        // TODO 5: Exception chaining — preserve original cause
        //   - try {
        //       connectToDatabase();
        //     } catch (SQLException e) {
        //       throw new AppException("Failed to load user data", e);  // e is the cause
        //     }
        //   - class AppException extends RuntimeException {
        //       AppException(String msg, Throwable cause) { super(msg, cause); }
        //     }
        //   - e.getCause() retrieves original exception; getCause().getMessage() for original message
        //   - Full stack trace printed with e.printStackTrace() includes "Caused by:" chain

        // TODO 6: throws declaration — when to declare vs catch
        //   - void readFile(String path) throws IOException { ... }   // declare checked exceptions
        //   - Rules: declare if you cannot handle it meaningfully; let caller decide
        //   - Override rules: subclass method may declare FEWER or NARROWER checked exceptions
        //   - Unchecked exceptions do NOT need to be declared (but documenting with @throws is good practice)

        // TODO 7: Result pattern — no-exception error handling
        //   - class Result<T> {
        //       private final T value;
        //       private final String error;
        //       private Result(T value, String error) { this.value = value; this.error = error; }
        //       static <T> Result<T> success(T value) { return new Result<>(value, null); }
        //       static <T> Result<T> failure(String error) { return new Result<>(null, error); }
        //       boolean isSuccess() { return error == null; }
        //       T getValue() { if (!isSuccess()) throw new IllegalStateException("Result is failure"); return value; }
        //       String getError() { return error; }
        //       <U> Result<U> map(java.util.function.Function<T,U> f) {
        //           return isSuccess() ? Result.success(f.apply(value)) : Result.failure(error);
        //       }
        //     }
        //   - Use: Result<Integer> r = parse("42"); r.map(n -> n * 2).getValue();

        // TODO 8: Logging — java.util.logging
        //   - Logger logger = Logger.getLogger(ErrorHandling.class.getName());
        //   - Log levels (ascending severity): FINEST, FINER, FINE, CONFIG, INFO, WARNING, SEVERE
        //   - logger.info("App started");
        //   - logger.warning("Low memory");
        //   - logger.severe("Database connection failed");
        //   - logger.log(Level.SEVERE, "Error", exception);  // attach exception
        //   - Add FileHandler: FileHandler fh = new FileHandler("app.log", true);
        //     fh.setFormatter(new SimpleFormatter()); logger.addHandler(fh);
    }
}
