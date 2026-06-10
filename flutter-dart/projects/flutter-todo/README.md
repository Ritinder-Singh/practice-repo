# Flutter Todo App — Riverpod + SharedPreferences

## Setup

```bash
flutter create flutter_todo --platforms=ios,android,web
cd flutter_todo
# Add to pubspec.yaml:
# flutter_riverpod: ^2.4.0
# riverpod_annotation: ^2.3.0
# shared_preferences: ^2.2.0
# freezed_annotation: ^2.4.0   # optional, for immutable models
# dev: build_runner, freezed, riverpod_generator
flutter pub get
```

## What to Build

### Milestone 1 — Data Model
- [ ] `class TodoItem { final String id, title; final bool isDone; final DateTime createdAt; }`
- [ ] `copyWith` method for immutable updates
- [ ] JSON serialization: `fromJson` / `toJson`

### Milestone 2 — Riverpod Providers
- [ ] `todoListProvider` — `StateNotifierProvider<TodoNotifier, List<TodoItem>>`
- [ ] `TodoNotifier extends StateNotifier<List<TodoItem>>` with:
  - `addTodo(String title)`
  - `toggleTodo(String id)`
  - `deleteTodo(String id)`
  - `reorderTodos(int oldIndex, int newIndex)`
- [ ] `filteredTodosProvider` — derived provider: filter by All/Active/Done

### Milestone 3 — Persistence
- [ ] `sharedPreferencesProvider` — `FutureProvider<SharedPreferences>`
- [ ] Load todos on app start; save on every state change
- [ ] Use `ref.listen(todoListProvider, (prev, next) => prefs.setString(...))`

### Milestone 4 — UI
- [ ] `TodoListScreen` — `ConsumerWidget` with `ListView.builder`
- [ ] Each tile: `CheckboxListTile`, swipe-to-delete with `Dismissible`
- [ ] FAB: show `AddTodoModal` bottom sheet
- [ ] Filter tabs at bottom: All / Active / Done
- [ ] Empty state illustration

### Milestone 5 — Polish
- [ ] Undo snackbar after delete: `ScaffoldMessenger.of(context).showSnackBar`
- [ ] Reorder list: `ReorderableListView`
- [ ] Theme toggle (light/dark) with `ThemeMode` in root provider
- [ ] App badge count (iOS/Android) showing active todos

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| Riverpod `StateNotifierProvider` | `providers/todo_provider.dart` — `TodoNotifier` |
| Derived / computed provider (`filteredTodosProvider`) | `providers/todo_provider.dart` |
| Immutable state model with `copyWith` | `TodoItem` class |
| JSON serialization (`fromJson` / `toJson`) | `TodoItem` class |
| `SharedPreferences` for local persistence | Milestone 3 |
| `ref.listen` side-effect trigger on state change | Milestone 3 |
| `Dismissible` widget for swipe-to-delete | `screens/todo_screen.dart` |
| `ReorderableListView` for drag-and-drop ordering | Milestone 5 |
| `ThemeMode` provider for light / dark toggle | Milestone 5 |
