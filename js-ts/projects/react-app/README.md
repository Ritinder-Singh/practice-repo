# React + TypeScript SPA

**Roadmap:** Framework Project — React + TypeScript SPA

## Setup
```bash
npm create vite@latest react-app -- --template react-ts
cd react-app && npm install
```

## TODO 1 (Mini): Component basics
- `ProductCard` component: name, price, "Add to Cart" button
- Props: `interface ProductCardProps { product: Product; onAdd: (id:number) => void }`
- Conditional rendering: "Out of Stock" badge when `stock === 0`
- CSS Modules for styling

## TODO 2 (Intermediate): State management
- Shopping cart with `useReducer`
- CartAction discriminated union: ADD_ITEM | REMOVE_ITEM | UPDATE_QTY | CLEAR_CART
- `useCart` custom hook + `CartContext` for global access
- `useMemo` for derived values (total price, item count)

## TODO 3 (Advanced): Data fetching + performance
- TanStack Query: `npm install @tanstack/react-query`
- Suspense + Error boundaries
- `React.memo`, `useCallback` optimizations
- Code splitting: `React.lazy` + `Suspense` per route

## Structure
```
src/components/ | src/hooks/ | src/pages/ | src/store/ | src/types/ | src/api/
```

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| TypeScript `interface` for component props | `ProductCardProps` in `components/` |
| Conditional rendering based on data state | "Out of Stock" badge when `stock === 0` |
| `useReducer` for multi-action state | Cart reducer |
| Discriminated union `CartAction` types | `store/cartReducer.ts` |
| Custom hook + `Context` for global cart state | `useCart` / `CartContext` |
| `useMemo` for derived computed values | cart total, item count |
| TanStack Query for server state and caching | TODO 3 |
| `Suspense` + Error boundaries | TODO 3 |
| `React.memo` + `useCallback` performance optimisation | TODO 3 |
| `React.lazy` + `Suspense` route-level code splitting | TODO 3 |
