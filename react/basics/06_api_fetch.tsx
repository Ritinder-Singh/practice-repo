// =============================================================================
// React / Next.js — Data Fetching & API
// =============================================================================
// Topics: Server Components (fetch in component), Client Components (useEffect/SWR),
//         React Query, route handlers (API routes), Prisma, caching.
// Docs: https://nextjs.org/docs/app/building-your-application/data-fetching
// =============================================================================

// ─── NEXT.JS SERVER COMPONENTS (preferred — no client JS needed) ──────────────

// TODO 1: fetch in a Server Component — the Next.js way
//   Server Components run on the server. No useEffect, no loading state needed.
//   Next.js extends fetch with caching options.
//
// async function PostList() {
//   const res = await fetch("https://jsonplaceholder.typicode.com/posts", {
//     next: { revalidate: 60 },  // ISR: revalidate every 60 seconds
//   });
//   const posts = await res.json();
//   return (
//     <ul>
//       {posts.map((p: Post) => <li key={p.id}>{p.title}</li>)}
//     </ul>
//   );
// }
//
//   Try each cache option:
//   { cache: "force-cache" }       — cache forever (static, like SSG)
//   { next: { revalidate: 60 } }   — ISR: refresh every 60s
//   { cache: "no-store" }          — always fresh (like SSR)

// TODO 2: Parallel data fetching — avoid waterfalls
//   BAD (sequential — slow):
//   const user = await fetchUser(id);
//   const posts = await fetchUserPosts(id);   // waits for user first
//
//   GOOD (parallel):
//   const [user, posts] = await Promise.all([fetchUser(id), fetchUserPosts(id)]);
//
//   Build a UserDashboard Server Component that fetches user + posts + stats in parallel.

// TODO 3: Route Handler (API route) — app/api/users/route.ts
//   Next.js App Router replaces pages/api/ with route handlers.
//
// import { NextRequest, NextResponse } from "next/server";
//
// export async function GET(request: NextRequest) {
//   const { searchParams } = new URL(request.url);
//   const page = Number(searchParams.get("page") ?? 1);
//   const users = await db.user.findMany({ skip: (page - 1) * 10, take: 10 });
//   return NextResponse.json({ users, page });
// }
//
// export async function POST(request: NextRequest) {
//   const body = await request.json();
//   const user = await db.user.create({ data: body });
//   return NextResponse.json(user, { status: 201 });
// }

// ─── CLIENT-SIDE FETCHING ─────────────────────────────────────────────────────

// TODO 4: useEffect + fetch (baseline client pattern)
//   Use when data must be client-fetched (e.g. user-specific, after interaction).
//   Create a SearchResults component that fetches when a debounced query changes.
//
// "use client";
// function SearchResults({ query }: { query: string }) {
//   const [results, setResults] = useState<Result[]>([]);
//   const [loading, setLoading] = useState(false);
//
//   useEffect(() => {
//     if (!query) return;
//     let cancelled = false;
//     setLoading(true);
//     fetch(`/api/search?q=${encodeURIComponent(query)}`)
//       .then(r => r.json())
//       .then(data => { if (!cancelled) setResults(data); })
//       .finally(() => { if (!cancelled) setLoading(false); });
//     return () => { cancelled = true; };
//   }, [query]);
// }

// TODO 5: SWR — stale-while-revalidate (lightweight, excellent DX)
//   import useSWR from "swr";
//   const fetcher = (url: string) => fetch(url).then(r => r.json());
//
// function UserCard({ userId }: { userId: number }) {
//   const { data, error, isLoading } = useSWR(`/api/users/${userId}`, fetcher);
//   if (isLoading) return <Spinner />;
//   if (error) return <p>Error: {error.message}</p>;
//   return <p>{data.name}</p>;
// }
//
//   Key features to understand and use:
//   - Automatic revalidation on focus
//   - Deduplication (same key → shared cache)
//   - useSWRMutation for POST/PUT/DELETE

// TODO 6: Prisma — database queries in Server Components
//   Prisma runs on the server only. Never import it in client components.
//
// import { PrismaClient } from "@prisma/client";
// const prisma = new PrismaClient();
//
// async function PostPage({ params }: { params: { id: string } }) {
//   const post = await prisma.post.findUnique({
//     where: { id: Number(params.id) },
//     include: { author: true, comments: { orderBy: { createdAt: "desc" } } },
//   });
//   if (!post) notFound();  // triggers Next.js 404 page
//   return <Article post={post} />;
// }
//
//   Practice: set up Prisma with PostgreSQL, write these queries:
//   - findUnique, findMany with where + orderBy + take
//   - create, update, delete
//   - include (eager load) vs select (projection)
