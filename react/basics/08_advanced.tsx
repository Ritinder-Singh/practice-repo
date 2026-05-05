// =============================================================================
// React / Next.js — Advanced Topics
// =============================================================================
// Topics: React Server Components, Server Actions, Suspense + streaming,
//         custom hooks, error boundaries, Next.js middleware, optimistic updates.
// Docs: https://react.dev/reference/react/Suspense
//       https://nextjs.org/docs/app/building-your-application/rendering/server-components
// =============================================================================

// ─── REACT SERVER COMPONENTS (RSC) ────────────────────────────────────────────

// TODO 1: Server vs Client component — the boundary
//   Server Component (default in App Router): runs on server, can be async,
//   can query DB directly, zero JS sent to client.
//   Client Component ("use client"): runs in browser, can use hooks and events.
//
//   Rules:
//   - Server can import Client, but Client CANNOT import Server
//   - Pass Server data to Client via props
//   - Hooks (useState, useEffect) only work in Client components
//   - Event handlers (onClick) only work in Client components
//
//   Build a page where:
//   - The data-fetching shell is a Server Component (fast, no JS)
//   - Only the interactive "Like" button is a Client Component

// TODO 2: Suspense + streaming — progressive rendering
//   Wrap slow data-fetching components in <Suspense> to stream the page progressively.
//   Fast parts render immediately; slow parts stream in when ready.
//
// import { Suspense } from "react";
//
// export default function Dashboard() {
//   return (
//     <div>
//       <h1>Dashboard</h1>
//       <UserCard />                          {/* fast — renders immediately */}
//       <Suspense fallback={<StatsSkeleton />}>
//         <ExpensiveStats />                  {/* slow — streams in later */}
//       </Suspense>
//       <Suspense fallback={<FeedSkeleton />}>
//         <ActivityFeed />                    {/* also slow, independent */}
//       </Suspense>
//     </div>
//   );
// }
//
//   ExpensiveStats and ActivityFeed load in parallel — neither blocks the other.

// TODO 3: Custom hooks — extract + reuse stateful logic
//   Custom hooks let you extract logic shared across components.
//   Name must start with "use".
//
//   Build these custom hooks:
//
//   useDebounce<T>(value: T, delay: number): T
//   — returns a debounced version of value, useful for search inputs
//
//   useLocalStorage<T>(key: string, initialValue: T): [T, (value: T) => void]
//   — persists state to localStorage, syncs across tabs
//
//   useClickOutside(ref: RefObject<HTMLElement>, handler: () => void): void
//   — calls handler when user clicks outside the referenced element (for dropdowns)
//
//   useFetch<T>(url: string): { data: T | null; loading: boolean; error: Error | null }
//   — generic fetch wrapper with loading/error state

// TODO 4: Optimistic updates — instant UI feedback
//   Update the UI immediately, then sync with the server in the background.
//   If server fails, roll back to previous state.
//
// import { useOptimistic } from "react";
//
// function LikeButton({ postId, initialLikes }: { postId: number; initialLikes: number }) {
//   const [optimisticLikes, addOptimisticLike] = useOptimistic(
//     initialLikes,
//     (currentLikes, delta: number) => currentLikes + delta
//   );
//
//   async function handleLike() {
//     addOptimisticLike(1);         // instant UI update
//     await likePost(postId);       // actual server call
//     // if this throws, React rolls back optimisticLikes
//   }
//
//   return <button onClick={handleLike}>♥ {optimisticLikes}</button>;
// }

// TODO 5: Error boundaries — catch render errors
//   React error boundaries catch JS errors in the render tree.
//   Must be a class component (or use react-error-boundary library).
//
// import { ErrorBoundary } from "react-error-boundary";
//
// function App() {
//   return (
//     <ErrorBoundary
//       fallback={<p>Something went wrong.</p>}
//       onError={(error, info) => logToSentry(error, info)}
//     >
//       <BuggyComponent />
//     </ErrorBoundary>
//   );
// }
//
//   In Next.js App Router: use error.tsx files instead (simpler, automatic).

// TODO 6: Next.js Middleware — run code before every request
//   Middleware runs on the edge before the page renders.
//   Use cases: auth redirects, A/B testing, locale detection, rate limiting.
//
// import { NextRequest, NextResponse } from "next/server";
// import { verifyToken } from "./lib/auth";
//
// export function middleware(request: NextRequest) {
//   const token = request.cookies.get("session")?.value;
//   const isProtected = request.nextUrl.pathname.startsWith("/dashboard");
//
//   if (isProtected && !token) {
//     return NextResponse.redirect(new URL("/login", request.url));
//   }
//
//   return NextResponse.next();
// }
//
// export const config = {
//   matcher: ["/dashboard/:path*", "/api/protected/:path*"],
// };
//
//   Build middleware that:
//   - Redirects unauthenticated users from /dashboard to /login
//   - Redirects authenticated users away from /login to /dashboard
