import 'package:flutter/material.dart';
// import 'package:flutter_riverpod/flutter_riverpod.dart';

// TODO 1: TodoListScreen — ConsumerWidget
//   class TodoListScreen extends ConsumerWidget {
//     @override
//     Widget build(BuildContext context, WidgetRef ref) {
//       final todos = ref.watch(filteredTodosProvider);
//       return Scaffold(
//         appBar: AppBar(title: const Text("Todos"), actions: [_filterButton(ref)]),
//         body: todos.isEmpty ? _emptyState() : _todoList(todos, ref),
//         floatingActionButton: FloatingActionButton(
//           onPressed: () => _showAddTodoSheet(context, ref),
//           child: const Icon(Icons.add),
//         ),
//       );
//     }
//   }

// TODO 2: _todoList — ListView with Dismissible for swipe-to-delete
//   Widget _todoList(List<TodoItem> todos, WidgetRef ref) {
//     return ListView.builder(
//       itemCount: todos.length,
//       itemBuilder: (ctx, i) {
//         final todo = todos[i];
//         return Dismissible(
//           key: ValueKey(todo.id),
//           direction: DismissDirection.endToStart,
//           background: Container(color: Colors.red, child: const Icon(Icons.delete, color: Colors.white)),
//           onDismissed: (_) {
//             ref.read(todoListProvider.notifier).deleteTodo(todo.id);
//             ScaffoldMessenger.of(ctx).showSnackBar(SnackBar(content: Text("Deleted: ${todo.title}")));
//           },
//           child: CheckboxListTile(
//             value: todo.isDone,
//             onChanged: (_) => ref.read(todoListProvider.notifier).toggleTodo(todo.id),
//             title: Text(todo.title, style: TextStyle(decoration: todo.isDone ? TextDecoration.lineThrough : null)),
//           ),
//         );
//       },
//     );
//   }

// TODO 3: _showAddTodoSheet — bottom sheet with TextField
//   void _showAddTodoSheet(BuildContext context, WidgetRef ref) {
//     final controller = TextEditingController();
//     showModalBottomSheet(context: context, builder: (ctx) => Padding(
//       padding: EdgeInsets.only(bottom: MediaQuery.of(ctx).viewInsets.bottom, left: 16, right: 16, top: 16),
//       child: Row(children: [
//         Expanded(child: TextField(controller: controller, autofocus: true, decoration: const InputDecoration(hintText: "New todo..."))),
//         IconButton(icon: const Icon(Icons.send), onPressed: () {
//           if (controller.text.isNotEmpty) {
//             ref.read(todoListProvider.notifier).addTodo(controller.text);
//             Navigator.pop(ctx);
//           }
//         }),
//       ]),
//     ));
//   }

class TodoListScreen extends StatelessWidget {
  const TodoListScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return const Scaffold(body: Center(child: Text("TODO: implement TodoListScreen")));
  }
}
