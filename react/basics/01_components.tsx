// =============================================================================
// React / Next.js — Components & JSX
// =============================================================================
// Topics: function components, JSX rules, props, prop types, children,
//         composition, conditional rendering, lists & keys.
// Run: paste into https://stackblitz.com/edit/react-ts or a Vite React app
// Docs: https://react.dev/learn/your-first-component
// =============================================================================

// TODO 1: Basic function component
//   Create a Greeting component that accepts a `name` prop (string)
//   and an optional `formal` prop (boolean, default false).
//   If formal: "Good day, {name}." — else: "Hey, {name}!"
//
// interface GreetingProps {
//   name: string;
//   formal?: boolean;
// }
// function Greeting({ name, formal = false }: GreetingProps) { ... }

// TODO 2: Children prop — Layout wrapper component
//   Create a Card component that wraps its children in a styled div.
//   Accept an optional `title` string that renders as a heading if provided.
//
// interface CardProps {
//   title?: string;
//   children: React.ReactNode;
// }
// function Card({ title, children }: CardProps) { ... }

// TODO 3: Conditional rendering
//   Create a StatusBadge component that renders differently based on status:
//   "active"  → green badge
//   "pending" → yellow badge
//   "error"   → red badge
//   Use a lookup object (not if/else chains) for the color map.
//
// type Status = "active" | "pending" | "error";
// interface StatusBadgeProps { status: Status; }
// function StatusBadge({ status }: StatusBadgeProps) { ... }

// TODO 4: Lists and keys
//   Create a UserList component that renders a list of users.
//   Each user has: id (number), name (string), email (string).
//   Key rule: always use a stable unique id, not array index.
//
// interface User { id: number; name: string; email: string; }
// interface UserListProps { users: User[]; }
// function UserList({ users }: UserListProps) { ... }

// TODO 5: Component composition
//   Build a ProfileCard composed of: Avatar + UserInfo + ActionButton.
//   Each sub-component is small and focused (single responsibility).
//   Props flow down — no shared state yet.
//
// function Avatar({ src, alt }: { src: string; alt: string }) { ... }
// function UserInfo({ name, role }: { name: string; role: string }) { ... }
// function ActionButton({ label, onClick }: { label: string; onClick: () => void }) { ... }
// function ProfileCard({ user }: { user: UserProfile }) { ... }

// TODO 6: JSX rules to internalize
//   - Return one root element (or <> fragment)
//   - className not class, htmlFor not for
//   - self-close empty tags: <img />, <input />
//   - JS expressions in {}, not statements
//   - style prop takes an object: style={{ color: "red", fontSize: 14 }}
//
//   Fix the broken JSX below:
// const broken = (
//   <div class="container">
//     <label for="name">Name</label>
//     <input type="text" id="name">
//     <img src="avatar.png">
//     <p style="color: red">Error</p>
//   </div>
// );

// TODO 7: Render a mini app
//   Compose your components above into an App that renders:
//   - A Card with title "Team" containing a UserList of 3 hardcoded users
//   - A ProfileCard for one of those users
