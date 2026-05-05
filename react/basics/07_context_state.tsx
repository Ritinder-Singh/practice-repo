// =============================================================================
// React / Next.js — Context & Global State
// =============================================================================
// Topics: Context API (createContext, useContext), when NOT to use context,
//         Zustand (lightweight global state), prop drilling vs context vs state lib.
// Docs: https://react.dev/reference/react/useContext
//       https://zustand.docs.pmnd.rs
// =============================================================================
import { createContext, useContext, useState, ReactNode } from "react";

// ─── CONTEXT API ──────────────────────────────────────────────────────────────

// TODO 1: Theme context — dark/light mode
//   The classic context use case: theme that any component in the tree needs.
//
// interface ThemeContextType {
//   theme: "light" | "dark";
//   toggleTheme: () => void;
// }
//
// const ThemeContext = createContext<ThemeContextType | null>(null);
//
// function ThemeProvider({ children }: { children: ReactNode }) {
//   const [theme, setTheme] = useState<"light" | "dark">("light");
//   const toggleTheme = () => setTheme(t => t === "light" ? "dark" : "light");
//   return (
//     <ThemeContext.Provider value={{ theme, toggleTheme }}>
//       {children}
//     </ThemeContext.Provider>
//   );
// }
//
// function useTheme() {
//   const ctx = useContext(ThemeContext);
//   if (!ctx) throw new Error("useTheme must be used within ThemeProvider");
//   return ctx;
// }
//
//   Wrap your app in ThemeProvider. Build a ThemeToggle button using useTheme().
//   Apply the theme class to the root <body> element.

// TODO 2: Auth context — current user everywhere
//   Build an AuthContext that holds: user | null, login(), logout(), isLoading.
//   Any component can call useAuth() to get the current user without prop drilling.
//
// interface AuthContextType {
//   user: User | null;
//   login: (email: string, password: string) => Promise<void>;
//   logout: () => void;
//   isLoading: boolean;
// }
//
//   Usage:
//   function Header() {
//     const { user, logout } = useAuth();
//     return user ? <button onClick={logout}>Logout {user.name}</button> : <Link href="/login">Login</Link>;
//   }

// TODO 3: When NOT to use context
//   Context re-renders every consumer when the value changes.
//   Use context for: auth, theme, locale — things that change rarely and are needed everywhere.
//   Do NOT use context for: frequently updating state (forms, animations, search queries).
//   For those, use local state or Zustand.
//
//   Demonstrate the re-render problem:
//   - Create a context with a counter that increments every second
//   - Show that ALL consumers re-render every second (add console.log to each)
//   - Fix with useMemo on the context value, or split into separate contexts

// ─── ZUSTAND ──────────────────────────────────────────────────────────────────

// TODO 4: Zustand — global state without providers
//   Zustand is ~1KB, no boilerplate, no providers, works outside React.
//
// import { create } from "zustand";
//
// interface CartStore {
//   items: CartItem[];
//   addItem: (item: CartItem) => void;
//   removeItem: (id: string) => void;
//   clearCart: () => void;
//   total: () => number;
// }
//
// const useCartStore = create<CartStore>((set, get) => ({
//   items: [],
//   addItem: (item) => set(state => ({ items: [...state.items, item] })),
//   removeItem: (id) => set(state => ({ items: state.items.filter(i => i.id !== id) })),
//   clearCart: () => set({ items: [] }),
//   total: () => get().items.reduce((sum, i) => sum + i.price * i.quantity, 0),
// }));
//
//   Build a shopping cart UI using this store:
//   - ProductCard with "Add to cart" button
//   - CartSidebar showing items and total
//   - CartBadge in header showing item count

// TODO 5: Zustand with persistence
//   Persist cart to localStorage automatically using the persist middleware:
//
// import { persist } from "zustand/middleware";
//
// const useCartStore = create<CartStore>()(
//   persist(
//     (set, get) => ({ ... }),
//     { name: "cart-storage" }  // localStorage key
//   )
// );
//
//   Verify: add items, refresh the page — items should still be there.

// TODO 6: Selectors — avoid unnecessary re-renders with Zustand
//   Only subscribe to the slice of state you need:
//
//   const itemCount = useCartStore(state => state.items.length);   // only re-renders when count changes
//   const total = useCartStore(state => state.total());             // only re-renders when total changes
//
//   vs — subscribes to entire store (re-renders on any store change):
//   const { items, addItem, total } = useCartStore();
//
//   Build a CartBadge that ONLY re-renders when item count changes, nothing else.
