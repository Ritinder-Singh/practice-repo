# Flutter E-Commerce App — BLoC + Multi-Platform

## Architecture: BLoC Pattern

```
UI (Widgets) ←→ BLoC ←→ Repository ←→ API / Local DB
     (Events)      (States)  (Protocol)
```

## Setup

```bash
flutter create ecommerce --platforms=ios,android,web
cd ecommerce
# pubspec.yaml additions:
# flutter_bloc: ^8.1.3
# bloc: ^8.1.2
# go_router: ^12.0.0
# dio: ^5.3.3
# hive_flutter: ^1.1.0
# hive_generator + build_runner (dev)
# cached_network_image: ^3.3.0
flutter pub get
```

## What to Build

### Milestone 1 — Product Catalog
- [ ] `Product` model: id, title, price, imageUrl, category, rating, stockCount
- [ ] `ProductRepository` protocol + `ApiProductRepository` implementation using dio
- [ ] `ProductBloc` with events: `LoadProducts`, `SearchProducts`, `FilterByCategory`
- [ ] States: `ProductInitial`, `ProductLoading`, `ProductLoaded(products)`, `ProductError(message)`
- [ ] `ProductListScreen` with GridView, search bar, category chips

### Milestone 2 — Cart
- [ ] `CartItem` model: product, quantity
- [ ] `CartBloc` with events: `AddToCart`, `RemoveFromCart`, `UpdateQuantity`, `ClearCart`
- [ ] States: `CartState(items: List<CartItem>, total: double)`
- [ ] `CartScreen` with item list, quantity controls, order total
- [ ] Badge on cart icon showing item count (BlocBuilder)

### Milestone 3 — Auth
- [ ] `AuthBloc`: `Login(email, password)`, `Logout`, `CheckAuth` events
- [ ] Secure storage for JWT token (flutter_secure_storage)
- [ ] Route guard: redirect to login if unauthenticated

### Milestone 4 — Navigation (go_router)
- [ ] Routes: `/`, `/products/:id`, `/cart`, `/checkout`, `/profile`, `/login`
- [ ] ShellRoute for bottom navigation bar
- [ ] Redirect logic based on auth state

### Milestone 5 — Local Cache (Hive)
- [ ] Cache product list in HiveBox; show cached while reloading
- [ ] Cache cart state; restore on app restart
- [ ] Search history: recent queries

### Milestone 6 — Checkout Flow
- [ ] `OrderBloc`: `PlaceOrder` event, `OrderConfirmed(orderId)` state
- [ ] Delivery address form with validation
- [ ] Payment stub (Stripe Flutter SDK integration)
- [ ] Order confirmation screen with animation

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| BLoC pattern (Events → BLoC → States) | `ProductBloc`, `CartBloc`, `AuthBloc` |
| Discriminated union action types | `CartAction` (ADD_ITEM / REMOVE_ITEM / UPDATE_QTY / CLEAR_CART) |
| Repository protocol + concrete API implementation | `ProductRepository` / `ApiProductRepository` |
| `dio` HTTP client for REST calls | `ApiProductRepository` |
| `Hive` local storage for offline product cache | Milestone 5 |
| `go_router` with `ShellRoute` for bottom navigation | Milestone 4 |
| JWT token stored in `flutter_secure_storage` | `AuthBloc` |
| Route guard (redirect to login if unauthenticated) | `go_router` redirect logic |
| `BlocBuilder` for reactive UI updates (cart badge) | Cart icon badge |
