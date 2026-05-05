// =============================================================================
// React / Next.js — useEffect & Lifecycle
// =============================================================================
// Topics: useEffect, dependency array, cleanup, strict mode double-invoke,
//         useMemo, useCallback, useRef.
// Docs: https://react.dev/reference/react/useEffect
// =============================================================================
import { useState, useEffect, useMemo, useCallback, useRef } from "react";

// TODO 1: useEffect dependency array rules
//   Explain what each of these does and when the effect runs:
//
//   useEffect(() => { ... })                    // A: runs after every render
//   useEffect(() => { ... }, [])               // B: runs once on mount
//   useEffect(() => { ... }, [count, userId])  // C: runs when count or userId changes
//
//   Implement a Clock component that shows the current time (updates every second).
//   The interval MUST be cleaned up when the component unmounts.
//
// function Clock() {
//   const [time, setTime] = useState(new Date());
//   useEffect(() => {
//     const id = setInterval(() => setTime(new Date()), 1000);
//     return () => clearInterval(id);  // cleanup!
//   }, []);
//   ...
// }

// TODO 2: Data fetching with useEffect
//   Create a UserProfile component that fetches a user from:
//   https://jsonplaceholder.typicode.com/users/{id}
//   Props: { userId: number }
//   States needed: data, loading, error
//   Handle: stale closures — if userId changes before fetch resolves, ignore the old response.
//
// function UserProfile({ userId }: { userId: number }) {
//   const [user, setUser] = useState<User | null>(null);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState<string | null>(null);
//   useEffect(() => {
//     let cancelled = false;   // <-- stale response guard
//     setLoading(true);
//     fetch(`...`)
//       .then(r => r.json())
//       .then(data => { if (!cancelled) setUser(data); })
//       .catch(e => { if (!cancelled) setError(e.message); })
//       .finally(() => { if (!cancelled) setLoading(false); });
//     return () => { cancelled = true; };
//   }, [userId]);
// }

// TODO 3: useRef — DOM reference and mutable values
//   Part A: focus an input on mount using useRef
//   const inputRef = useRef<HTMLInputElement>(null);
//   useEffect(() => { inputRef.current?.focus(); }, []);
//
//   Part B: useRef as an instance variable (survives renders without causing re-render)
//   Create a component that counts renders without useState (which would cause infinite loop):
//   const renderCount = useRef(0);
//   renderCount.current++;   // NOT state — won't trigger re-render

// TODO 4: useMemo — expensive computations
//   Given a list of 10,000 numbers and a filter input:
//   - Compute filtered + sorted list — this is expensive
//   - Only recompute when the list or filter changes, not on every render
//
// function ExpensiveList({ numbers }: { numbers: number[] }) {
//   const [filter, setFilter] = useState("");
//   const processed = useMemo(() => {
//     return numbers
//       .filter(n => n.toString().includes(filter))
//       .sort((a, b) => a - b);
//   }, [numbers, filter]);
// }

// TODO 5: useCallback — stable function references
//   Why it matters: without useCallback, a new function is created each render,
//   causing child components wrapped in React.memo to re-render anyway.
//
//   Create a parent with useCallback-wrapped handler passed to a memoized child:
//
// const Child = React.memo(({ onClick }: { onClick: () => void }) => {
//   console.log("Child rendered");
//   return <button onClick={onClick}>Click</button>;
// });
//
// function Parent() {
//   const [count, setCount] = useState(0);
//   const [other, setOther] = useState(0);
//   const handleClick = useCallback(() => setCount(c => c + 1), []);
//   // Child should NOT re-render when `other` changes
// }

// TODO 6: React.memo — skip re-rendering unchanged children
//   Without memo: every parent re-render re-renders all children.
//   Wrap an expensive component in React.memo to only re-render when its props change.
//   Combine with useCallback for handlers and useMemo for derived data props.
