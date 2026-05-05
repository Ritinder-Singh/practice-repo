import 'package:flutter/material.dart';
// import 'package:flutter_bloc/flutter_bloc.dart';
// import 'package:go_router/go_router.dart';

// TODO 1: MultiBlocProvider setup at root
//   void main() async {
//     WidgetsFlutterBinding.ensureInitialized();
//     await Hive.initFlutter();
//     runApp(const EcommerceApp());
//   }

// TODO 2: EcommerceApp with MultiBlocProvider
//   class EcommerceApp extends StatelessWidget {
//     @override
//     Widget build(BuildContext context) {
//       return MultiBlocProvider(
//         providers: [
//           BlocProvider(create: (_) => AuthBloc()..add(CheckAuth())),
//           BlocProvider(create: (_) => ProductBloc(ProductRepository())..add(LoadProducts())),
//           BlocProvider(create: (_) => CartBloc()),
//         ],
//         child: BlocListener<AuthBloc, AuthState>(
//           listener: (ctx, state) { /* redirect on auth change */ },
//           child: MaterialApp.router(routerConfig: appRouter),
//         ),
//       );
//     }
//   }

// TODO 3: GoRouter configuration
//   final appRouter = GoRouter(
//     routes: [
//       ShellRoute(
//         builder: (ctx, state, child) => MainScaffold(child: child),
//         routes: [
//           GoRoute(path: '/', builder: (ctx, state) => ProductListScreen()),
//           GoRoute(path: '/cart', builder: (ctx, state) => CartScreen()),
//           GoRoute(path: '/profile', builder: (ctx, state) => ProfileScreen()),
//         ],
//       ),
//       GoRoute(path: '/products/:id', builder: (ctx, state) => ProductDetailScreen(id: state.pathParameters['id']!)),
//       GoRoute(path: '/login', builder: (ctx, state) => LoginScreen()),
//     ],
//   );

void main() {
  runApp(const MaterialApp(home: Scaffold(body: Center(child: Text("TODO: implement E-Commerce app")))));
}
