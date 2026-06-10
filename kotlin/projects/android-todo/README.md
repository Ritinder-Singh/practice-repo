# Android Todo App — Jetpack Compose + MVVM + Room

## Setup

1. Open Android Studio → New Project → Empty Activity (Compose)
2. Minimum SDK: API 26 (Android 8)
3. Add dependencies in `build.gradle.kts`:
   ```kotlin
   // Room
   implementation("androidx.room:room-runtime:2.6.1")
   ksp("androidx.room:room-compiler:2.6.1")
   implementation("androidx.room:room-ktx:2.6.1")
   // ViewModel + Compose
   implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.7.0")
   implementation("androidx.compose.material3:material3:1.2.0")
   // Navigation
   implementation("androidx.navigation:navigation-compose:2.7.5")
   ```

## What to Build

### Milestone 1 — Data Layer
- [ ] `data class TodoItem(val id: Int, val title: String, val isDone: Boolean, val createdAt: Long)`
- [ ] `@Entity` annotation on TodoItem, `@PrimaryKey(autoGenerate=true)`
- [ ] `@Dao interface TodoDao` with `@Insert`, `@Update`, `@Delete`, `@Query("SELECT * FROM todo_items ORDER BY createdAt DESC")`
- [ ] `@Database abstract class AppDatabase : RoomDatabase()` with `abstract fun todoDao(): TodoDao`

### Milestone 2 — ViewModel
- [ ] `class TodoViewModel(private val dao: TodoDao) : ViewModel()`
- [ ] `val todos: StateFlow<List<TodoItem>>` from `dao.getAllTodos()` via `stateIn`
- [ ] `fun addTodo(title: String)` — `viewModelScope.launch { dao.insert(TodoItem(...)) }`
- [ ] `fun toggleDone(item: TodoItem)` — `dao.update(item.copy(isDone = !item.isDone))`
- [ ] `fun deleteTodo(item: TodoItem)` — `dao.delete(item)`

### Milestone 3 — UI (Compose)
- [ ] `TodoListScreen` — `LazyColumn` of `TodoItem` rows
- [ ] Each row: `Checkbox`, `Text`, swipe-to-delete with `SwipeToDismiss`
- [ ] FAB for adding new todos — show `AddTodoSheet` (bottom sheet)
- [ ] `AddTodoSheet` — `TextField`, "Add" button, dismiss on success

### Milestone 4 — Navigation
- [ ] `NavHost` with routes: `"list"` → `"detail/{id}"`
- [ ] Detail screen showing full todo info + edit button

### Milestone 5 — Polish
- [ ] Dark/light theme toggle stored in `DataStore`
- [ ] Undo delete with `Snackbar`
- [ ] Filter tabs: All / Active / Done

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| Room `@Entity` + auto-increment `@PrimaryKey` | `TodoItem` data class |
| `@Dao` interface with `@Insert`, `@Update`, `@Delete`, `@Query` | `TodoDao` |
| `@Database` abstract class wiring DAOs | `AppDatabase` |
| KSP annotation processor for Room code generation | `build.gradle.kts` |
| `ViewModel` + `viewModelScope.launch` coroutines | `TodoViewModel` |
| `StateFlow` + `stateIn` for reactive Compose UI | `todos: StateFlow<List<TodoItem>>` |
| Jetpack Compose `LazyColumn` + `SwipeToDismiss` | `TodoListScreen` |
| Compose `NavHost` with typed routes | Milestone 4 |
| `DataStore` for persisting user preferences (theme) | Milestone 5 |
