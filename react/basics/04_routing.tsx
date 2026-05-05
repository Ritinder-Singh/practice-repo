// =============================================================================
// React / Next.js — Routing
// =============================================================================
// Topics: Next.js App Router (file-system routing), layouts, dynamic routes,
//         Link, useRouter, usePathname, route groups, loading/error boundaries.
// Docs: https://nextjs.org/docs/app/building-your-application/routing
// =============================================================================

// ─── NEXT.JS APP ROUTER (primary — used in production) ────────────────────────

// TODO 1: File-system routing — understand the conventions
//
//   app/
//     layout.tsx          → root layout, wraps all pages
//     page.tsx            → renders at "/"
//     about/
//       page.tsx          → renders at "/about"
//     blog/
//       page.tsx          → renders at "/blog"
//       [slug]/
//         page.tsx        → renders at "/blog/:slug" (dynamic segment)
//     (auth)/             → route group — doesn't appear in URL
//       login/page.tsx    → renders at "/login"
//       register/page.tsx → renders at "/register"
//     api/
//       users/route.ts    → API route at "/api/users" (GET, POST, etc.)
//
//   Create this structure in a new Next.js project. Verify each URL works.

// TODO 2: Link component — client-side navigation
//   Never use <a href> for internal links in Next.js — it causes full page reload.
//   Use <Link> for instant client-side navigation with prefetching.
//
// import Link from "next/link";
//
// function Navbar() {
//   return (
//     <nav>
//       <Link href="/">Home</Link>
//       <Link href="/about">About</Link>
//       <Link href="/blog">Blog</Link>
//     </nav>
//   );
// }

// TODO 3: Dynamic routes — params
//   In app/blog/[slug]/page.tsx, the component receives params as a prop:
//
// interface PageProps {
//   params: { slug: string };
// }
//
// export default function BlogPost({ params }: PageProps) {
//   return <h1>Post: {params.slug}</h1>;
// }
//
//   Extension: catch-all routes app/docs/[...path]/page.tsx
//   params.path is an array: ["guide", "installation"] for /docs/guide/installation

// TODO 4: useRouter and usePathname
//   Both are client-side hooks — only work in "use client" components.
//
// "use client";
// import { useRouter, usePathname } from "next/navigation";
//
// function NavigationExample() {
//   const router = useRouter();
//   const pathname = usePathname();  // current URL path
//
//   return (
//     <>
//       <p>Current path: {pathname}</p>
//       <button onClick={() => router.push("/about")}>Go to About</button>
//       <button onClick={() => router.back()}>Go Back</button>
//       <button onClick={() => router.refresh()}>Refresh (re-run server fetch)</button>
//     </>
//   );
// }

// TODO 5: Layouts — shared UI across routes
//   Layouts persist between navigations (not re-mounted).
//   Root layout (app/layout.tsx) is required and wraps everything.
//
// export default function RootLayout({ children }: { children: React.ReactNode }) {
//   return (
//     <html lang="en">
//       <body>
//         <Navbar />         {/* persists across all routes */}
//         <main>{children}</main>
//         <Footer />
//       </body>
//     </html>
//   );
// }
//
//   Create a nested layout for /dashboard/* that shows a sidebar.

// TODO 6: loading.tsx and error.tsx — built-in boundaries
//   Place these files alongside page.tsx to auto-wrap with Suspense/ErrorBoundary.
//
//   app/blog/loading.tsx   → shows while page.tsx is suspending (streaming)
//   app/blog/error.tsx     → shows when page.tsx throws an error
//
// "use client";  // error.tsx must be a client component
// export default function Error({ error, reset }: { error: Error; reset: () => void }) {
//   return (
//     <div>
//       <p>Something went wrong: {error.message}</p>
//       <button onClick={reset}>Try again</button>
//     </div>
//   );
// }

// TODO 7: Active link styling — highlight current route
//   Build a NavLink component that adds "active" class when its href matches the current path.
//
// "use client";
// import Link from "next/link";
// import { usePathname } from "next/navigation";
//
// function NavLink({ href, children }: { href: string; children: React.ReactNode }) {
//   const pathname = usePathname();
//   const isActive = pathname === href;
//   return (
//     <Link href={href} className={isActive ? "nav-link active" : "nav-link"}>
//       {children}
//     </Link>
//   );
// }
