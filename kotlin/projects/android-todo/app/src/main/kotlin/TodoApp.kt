// PROJECT: Android Todo App — Compose Entry Point

// TODO 1: @AndroidEntryPoint MainActivity (or standard ComponentActivity)
//   class MainActivity : ComponentActivity() {
//       override fun onCreate(savedInstanceState: Bundle?) {
//           super.onCreate(savedInstanceState)
//           setContent {
//               TodoTheme {
//                   Surface { TodoNavHost() }
//               }
//           }
//       }
//   }

// TODO 2: TodoNavHost composable
//   @Composable
//   fun TodoNavHost(navController: NavHostController = rememberNavController()) {
//       NavHost(navController, startDestination = "list") {
//           composable("list") { TodoListScreen(navController) }
//           composable("detail/{id}") { backStack ->
//               val id = backStack.arguments?.getString("id")?.toInt()
//               TodoDetailScreen(id, navController)
//           }
//       }
//   }

// TODO 3: Theme setup
//   @Composable
//   fun TodoTheme(darkTheme: Boolean = isSystemInDarkTheme(), content: @Composable () -> Unit) {
//       MaterialTheme(colorScheme = if (darkTheme) DarkColorScheme else LightColorScheme, content = content)
//   }

fun main() {
    println("TODO: implement Android Todo app")
}
