// =============================================================================
// PROJECT: TypeScript CLI Todo App
// =============================================================================
// TODO 1 (Mini): In-memory CRUD
//   add "text" | list | done <id> | delete <id> | clear (remove completed)
//
// TODO 2 (Intermediate): Persist to ~/.todos.json
//   due <id> 2024-12-31 | priority <id> high|med|low
//   list --sort=priority | list --filter=pending
//
// TODO 3 (Advanced): SQLite backend
//   npm install better-sqlite3
//   Full-text search, tags, stats command
//
// Run: npx ts-node todo_cli.ts add "Learn TypeScript"
// =============================================================================

interface Todo {
  id: number; text: string; done: boolean;
  priority: "high"|"medium"|"low";
  dueDate?: Date; tags: string[]; createdAt: Date;
}

class TodoStore {
  private todos: Todo[] = [];
  private nextId = 1;
  // TODO: add(text:string): Todo
  // TODO: list(filter?:Partial<Todo>): Todo[]
  // TODO: markDone(id:number): boolean
  // TODO: remove(id:number): boolean
  // TODO: save() / load() for JSON persistence
}

const [,, command, ...args] = process.argv;
const store = new TodoStore();
// TODO: dispatch command to store methods, print formatted output
console.log("Todo CLI — implement commands");
