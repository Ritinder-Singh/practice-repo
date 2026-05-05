import 'package:flutter/material.dart';
// import 'package:flutter_riverpod/flutter_riverpod.dart';

// TODO 1: Wrap app with ProviderScope
//   void main() {
//     runApp(const ProviderScope(child: TodoApp()));
//   }

// TODO 2: TodoApp root widget
//   class TodoApp extends ConsumerWidget {
//     const TodoApp({super.key});
//     @override
//     Widget build(BuildContext context, WidgetRef ref) {
//       return MaterialApp(
//         title: "Flutter Todo",
//         theme: ThemeData(colorSchemeSeed: Colors.indigo, useMaterial3: true),
//         darkTheme: ThemeData.dark(useMaterial3: true),
//         themeMode: ref.watch(themeModeProvider),
//         home: const TodoListScreen(),
//       );
//     }
//   }

// TODO 3: Theme mode provider
//   final themeModeProvider = StateProvider<ThemeMode>((ref) => ThemeMode.system);

void main() {
  runApp(const MaterialApp(home: Scaffold(body: Center(child: Text("TODO: implement Todo app")))));
}
