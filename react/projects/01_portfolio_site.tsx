// =============================================================================
// Project: Portfolio Site (mini)
// Stack: Next.js App Router + Tailwind CSS
// Goal: Build and deploy a personal portfolio with server-rendered pages.
// =============================================================================

// ─── STRUCTURE TO BUILD ───────────────────────────────────────────────────────
//
//   app/
//     layout.tsx          — root layout with Navbar + Footer
//     page.tsx            — hero section + featured projects
//     about/page.tsx      — bio, skills, timeline
//     projects/
//       page.tsx          — all projects grid
//       [slug]/page.tsx   — individual project detail
//     contact/page.tsx    — contact form (Server Action)
//   components/
//     Navbar.tsx
//     ProjectCard.tsx
//     SkillBadge.tsx
//   lib/
//     projects.ts         — static data or CMS fetch

// ─── TODO 1: Root layout with Navbar ─────────────────────────────────────────
//
// export default function RootLayout({ children }: { children: React.ReactNode }) {
//   return (
//     <html lang="en">
//       <body className="bg-gray-950 text-white">
//         <Navbar />
//         <main className="mx-auto max-w-5xl px-6 py-12">{children}</main>
//         <Footer />
//       </body>
//     </html>
//   );
// }

// ─── TODO 2: Projects data (static) ──────────────────────────────────────────
//
// export const projects = [
//   {
//     slug: "secondbrain",
//     title: "SecondBrain",
//     description: "Local RAG AI assistant — privacy-first knowledge base.",
//     tags: ["Python", "Ollama", "FastAPI", "Docker"],
//     github: "https://github.com/Ritinder-Singh/secondbrain",
//     demo: null,
//   },
//   {
//     slug: "pixelpod",
//     title: "PixelPod",
//     description: "Self-hosted music manager with iPod sync.",
//     tags: ["Flutter", "FastAPI", "Jenkins", "Raspberry Pi"],
//     github: "https://github.com/Ritinder-Singh/PixelPod",
//     demo: null,
//   },
// ];
//
// export function getProjectBySlug(slug: string) {
//   return projects.find(p => p.slug === slug) ?? null;
// }

// ─── TODO 3: ProjectCard component ───────────────────────────────────────────
//
// interface ProjectCardProps {
//   title: string;
//   description: string;
//   tags: string[];
//   github?: string;
//   demo?: string;
//   slug: string;
// }
//
// function ProjectCard({ title, description, tags, github, demo, slug }: ProjectCardProps) {
//   return (
//     <Link href={`/projects/${slug}`} className="group block rounded-xl border border-gray-800 p-6 hover:border-gray-600 transition-colors">
//       <h3 className="text-lg font-semibold">{title}</h3>
//       <p className="mt-2 text-sm text-gray-400">{description}</p>
//       <div className="mt-4 flex flex-wrap gap-2">
//         {tags.map(tag => <span key={tag} className="text-xs bg-gray-800 px-2 py-1 rounded">{tag}</span>)}
//       </div>
//     </Link>
//   );
// }

// ─── TODO 4: Contact form with Server Action ──────────────────────────────────
//
// "use server";
// async function sendContactEmail(formData: FormData) {
//   const name = formData.get("name") as string;
//   const email = formData.get("email") as string;
//   const message = formData.get("message") as string;
//   // Send via Resend, SendGrid, etc.
//   await resend.emails.send({
//     from: "portfolio@yourdomain.com",
//     to: "for.ritindersingh@gmail.com",
//     subject: `Portfolio contact from ${name}`,
//     text: message,
//     replyTo: email,
//   });
// }

// ─── TODO 5: Deploy to Vercel ─────────────────────────────────────────────────
//   1. Push repo to GitHub
//   2. Import to vercel.com — zero config for Next.js
//   3. Add environment variables (DB URL, email API key)
//   4. Set up a custom domain
