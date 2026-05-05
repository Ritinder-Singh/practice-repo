// =============================================================================
// React / Next.js — State & Hooks
// =============================================================================
// Topics: useState, useReducer, state updates, immutability, batching,
//         derived state, lifting state up.
// Docs: https://react.dev/reference/react/useState
// =============================================================================
import { useState, useReducer } from "react";

// TODO 1: useState — counter with min/max bounds
//   Create a Counter component:
//   - Increment / Decrement buttons
//   - Reset button (back to initialValue)
//   - min and max props — buttons disable at bounds
//   - Show current value and how far from max
//
// interface CounterProps { initialValue?: number; min?: number; max?: number; }
// function Counter({ initialValue = 0, min = 0, max = 10 }: CounterProps) { ... }

// TODO 2: useState with objects — don't mutate!
//   Create a UserForm component with { name, email, age } state.
//   Update individual fields without spreading incorrectly.
//   Rule: always create a new object — never mutate state directly.
//
// interface UserState { name: string; email: string; age: number; }
// function UserForm() {
//   const [user, setUser] = useState<UserState>({ name: "", email: "", age: 0 });
//   // WRONG: user.name = "Alice"   <- mutation
//   // RIGHT: setUser({ ...user, name: "Alice" })
// }

// TODO 3: useState with arrays — add/remove/update
//   Create a TodoList component:
//   - Add new todo (input + button)
//   - Toggle complete (click item)
//   - Remove todo (delete button per item)
//   Forbidden: push(), splice(), direct index assignment
//
// interface Todo { id: number; text: string; done: boolean; }
// function TodoList() { ... }

// TODO 4: useReducer — same TodoList but with reducer
//   Replace the TodoList useState calls with a single useReducer.
//   Define a TodoAction union type: ADD_TODO | TOGGLE_TODO | DELETE_TODO
//   Reducer must be a pure function — same input always same output.
//
// type TodoAction =
//   | { type: "ADD_TODO"; payload: string }
//   | { type: "TOGGLE_TODO"; payload: number }
//   | { type: "DELETE_TODO"; payload: number };
//
// function todoReducer(state: Todo[], action: TodoAction): Todo[] { ... }

// TODO 5: Derived state — don't store what you can compute
//   In the TodoList above, add these WITHOUT adding new state:
//   - completedCount — how many todos are done
//   - allDone — boolean, true when every todo is complete
//   - filteredTodos — accepts a "all" | "active" | "done" filter prop
//   Key principle: if you can compute it from existing state, don't store it.

// TODO 6: Lifting state up
//   Build a TemperatureConverter with two inputs (Celsius ↔ Fahrenheit).
//   Both inputs stay in sync — changing one updates the other.
//   Rule: put state in the nearest common ancestor (the parent), not both children.
//
// function CelsiusInput({ celsius, onChange }: { celsius: number; onChange: (v: number) => void }) { ... }
// function FahrenheitInput({ fahrenheit, onChange }: { fahrenheit: number; onChange: (v: number) => void }) { ... }
// function TemperatureConverter() {
//   const [celsius, setCelsius] = useState(0);
//   // derive fahrenheit — don't store both
// }

// TODO 7: State initialiser function (lazy init)
//   When initial state is expensive to compute, pass a function to useState:
//   const [items, setItems] = useState(() => JSON.parse(localStorage.getItem("items") ?? "[]"));
//   The function runs only once — not on every render.
//
//   Create a component that initialises state from localStorage,
//   and persists changes back on every state update.
