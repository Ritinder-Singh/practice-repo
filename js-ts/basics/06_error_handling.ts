// =============================================================================
// TypeScript — Error Handling
// =============================================================================
// Topics: custom error classes, Result<T,E> pattern, discriminated union errors,
//         async error handling, error chaining.
// Run: npx ts-node 06_error_handling.ts
// =============================================================================

// TODO 1: Custom error hierarchy
//   class AppError extends Error {
//     constructor(message:string, public code:string) {
//       super(message);
//       this.name = this.constructor.name;
//       Object.setPrototypeOf(this, new.target.prototype); // fix instanceof
//     }
//   }
//   class ValidationError extends AppError {}
//   class NotFoundError extends AppError {}
//   class NetworkError extends AppError { constructor(msg:string, public status:number) { ... } }

// TODO 2: Result<T,E> type (no exceptions in caller)
//   type Ok<T>  = { ok: true;  value: T }
//   type Err<E> = { ok: false; error: E }
//   type Result<T,E> = Ok<T> | Err<E>
//   const ok  = <T>(v:T): Ok<T>  => ({ ok:true,  value:v })
//   const err = <E>(e:E): Err<E> => ({ ok:false, error:e })
//   Implement: parseJSON<T>(s:string): Result<T, SyntaxError>

// TODO 3: Discriminated union for API errors
//   type ApiError =
//     | { type:"network";    message:string }
//     | { type:"auth";       expiredAt:Date }
//     | { type:"validation"; fields:Record<string,string[]> }
//     | { type:"server";     statusCode:number }
//   function handleApiError(e:ApiError): string — switch on type, TypeScript enforces exhaustion

// TODO 4: Async Result pattern
//   async function safeAsync<T>(fn: ()=>Promise<T>): Promise<Result<T,Error>>
//   — wraps fn in try/catch, returns ok(value) or err(error)
//
//   async function fetchUser(id:number): Promise<Result<User, NotFoundError|NetworkError>>

// TODO 5: Error boundary higher-order function
//   function withErrorBoundary<T extends (...args:any[])=>any>(
//     fn: T, fallback: (e:Error) => ReturnType<T>
//   ): T
//   — wraps fn, catches synchronous errors, calls fallback
