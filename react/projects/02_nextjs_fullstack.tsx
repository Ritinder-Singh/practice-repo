// =============================================================================
// Project: Full-Stack Next.js App (major)
// Stack: Next.js App Router + Prisma ORM + PostgreSQL + NextAuth v5
// Goal: Full authentication, CRUD, DB — production-quality structure.
// =============================================================================

// ─── STRUCTURE TO BUILD ───────────────────────────────────────────────────────
//
//   app/
//     layout.tsx
//     page.tsx                     — public landing
//     (auth)/
//       login/page.tsx
//       register/page.tsx
//     dashboard/
//       layout.tsx                 — protected layout (check session)
//       page.tsx                   — user's items list
//       new/page.tsx               — create item form
//       [id]/
//         page.tsx                 — item detail
//         edit/page.tsx            — edit item
//   lib/
//     auth.ts                      — NextAuth config
//     db.ts                        — Prisma client singleton
//   prisma/
//     schema.prisma
//     migrations/

// ─── TODO 1: Prisma schema ────────────────────────────────────────────────────
//
// schema.prisma:
//
// generator client {
//   provider = "prisma-client-js"
// }
// datasource db {
//   provider = "postgresql"
//   url      = env("DATABASE_URL")
// }
// model User {
//   id        Int      @id @default(autoincrement())
//   email     String   @unique
//   name      String?
//   password  String
//   items     Item[]
//   createdAt DateTime @default(now())
// }
// model Item {
//   id          Int      @id @default(autoincrement())
//   title       String
//   description String?
//   done        Boolean  @default(false)
//   userId      Int
//   user        User     @relation(fields: [userId], references: [id], onDelete: Cascade)
//   createdAt   DateTime @default(now())
//   updatedAt   DateTime @updatedAt
// }
//
//   Run: npx prisma migrate dev --name init

// ─── TODO 2: Prisma client singleton (prevent hot-reload connection leaks) ────
//
// lib/db.ts:
// import { PrismaClient } from "@prisma/client";
// const globalForPrisma = globalThis as unknown as { prisma: PrismaClient };
// export const prisma = globalForPrisma.prisma ?? new PrismaClient();
// if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;

// ─── TODO 3: NextAuth v5 — credentials + session ─────────────────────────────
//
// lib/auth.ts:
// import NextAuth from "next-auth";
// import Credentials from "next-auth/providers/credentials";
// import bcrypt from "bcryptjs";
// import { prisma } from "./db";
//
// export const { auth, handlers, signIn, signOut } = NextAuth({
//   providers: [
//     Credentials({
//       async authorize(credentials) {
//         const user = await prisma.user.findUnique({ where: { email: credentials.email as string } });
//         if (!user) return null;
//         const valid = await bcrypt.compare(credentials.password as string, user.password);
//         return valid ? user : null;
//       },
//     }),
//   ],
//   callbacks: {
//     session({ session, token }) {
//       session.user.id = token.sub!;
//       return session;
//     },
//   },
// });

// ─── TODO 4: Protected dashboard layout ──────────────────────────────────────
//
// app/dashboard/layout.tsx:
// import { auth } from "@/lib/auth";
// import { redirect } from "next/navigation";
//
// export default async function DashboardLayout({ children }: { children: React.ReactNode }) {
//   const session = await auth();
//   if (!session) redirect("/login");
//   return <div className="dashboard-layout">{children}</div>;
// }

// ─── TODO 5: Server Action for creating an item ───────────────────────────────
//
// "use server";
// import { auth } from "@/lib/auth";
// import { prisma } from "@/lib/db";
// import { revalidatePath } from "next/cache";
// import { redirect } from "next/navigation";
//
// export async function createItem(formData: FormData) {
//   const session = await auth();
//   if (!session?.user?.id) throw new Error("Unauthorized");
//
//   const title = formData.get("title") as string;
//   if (!title?.trim()) throw new Error("Title is required");
//
//   await prisma.item.create({
//     data: { title, userId: Number(session.user.id) },
//   });
//
//   revalidatePath("/dashboard");
//   redirect("/dashboard");
// }

// ─── TODO 6: Dashboard page — list user's items ───────────────────────────────
//
// app/dashboard/page.tsx:
// import { auth } from "@/lib/auth";
// import { prisma } from "@/lib/db";
//
// export default async function DashboardPage() {
//   const session = await auth();
//   const items = await prisma.item.findMany({
//     where: { userId: Number(session!.user!.id) },
//     orderBy: { createdAt: "desc" },
//   });
//   return (
//     <div>
//       <h1>Your Items</h1>
//       <Link href="/dashboard/new">+ New Item</Link>
//       <ul>
//         {items.map(item => (
//           <li key={item.id}>
//             <Link href={`/dashboard/${item.id}`}>{item.title}</Link>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }
