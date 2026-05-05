// PROJECT: Todo Providers — Riverpod state management

// TODO 1: TodoItem model
//   class TodoItem {
//     final String id;
//     final String title;
//     final bool isDone;
//     final DateTime createdAt;
//
//     const TodoItem({required this.id, required this.title, this.isDone = false, required this.createdAt});
//
//     TodoItem copyWith({String? title, bool? isDone}) =>
//         TodoItem(id: id, title: title ?? this.title, isDone: isDone ?? this.isDone, createdAt: createdAt);
//
//     Map<String, dynamic> toJson() => {"id": id, "title": title, "isDone": isDone, "createdAt": createdAt.toIso8601String()};
//     factory TodoItem.fromJson(Map<String, dynamic> json) => TodoItem(
//           id: json["id"], title: json["title"], isDone: json["isDone"],
//           createdAt: DateTime.parse(json["createdAt"]));
//   }

// TODO 2: TodoNotifier
//   class TodoNotifier extends StateNotifier<List<TodoItem>> {
//     TodoNotifier() : super([]);
//
//     void addTodo(String title) {
//       state = [...state, TodoItem(id: DateTime.now().millisecondsSinceEpoch.toString(), title: title, createdAt: DateTime.now())];
//     }
//     void toggleTodo(String id) {
//       state = state.map((t) => t.id == id ? t.copyWith(isDone: !t.isDone) : t).toList();
//     }
//     void deleteTodo(String id) {
//       state = state.where((t) => t.id != id).toList();
//     }
//   }

// TODO 3: Providers
//   final todoListProvider = StateNotifierProvider<TodoNotifier, List<TodoItem>>((ref) => TodoNotifier());
//
//   enum TodoFilter { all, active, done }
//   final todoFilterProvider = StateProvider<TodoFilter>((ref) => TodoFilter.all);
//
//   final filteredTodosProvider = Provider<List<TodoItem>>((ref) {
//     final todos = ref.watch(todoListProvider);
//     final filter = ref.watch(todoFilterProvider);
//     return switch (filter) {
//       TodoFilter.all => todos,
//       TodoFilter.active => todos.where((t) => !t.isDone).toList(),
//       TodoFilter.done => todos.where((t) => t.isDone).toList(),
//     };
//   });
