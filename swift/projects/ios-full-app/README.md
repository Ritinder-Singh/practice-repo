# iOS Full App — CoreData + Combine + MVVM

## Architecture Overview

```
View ←→ ViewModel ←→ Repository ←→ CoreData / Network
         (Combine)    (Protocol)
```

## Setup

1. Xcode → New Project → App, with **Use Core Data** checked
2. Choose SwiftUI interface, Swift language
3. Target: iOS 17+

## What to Build

### Milestone 1 — CoreData Model
- [ ] `Note` entity: id (UUID), title (String), content (String), createdAt (Date), isPinned (Bool)
- [ ] `Tag` entity: id (UUID), name (String), color (String)
- [ ] Many-to-many relationship: Note ↔ Tag
- [ ] `NSPersistentContainer` in `PersistenceController` singleton

### Milestone 2 — Repository Layer (Protocol-based for testability)
- [ ] `protocol NoteRepository { func fetchAll() -> AnyPublisher<[Note], Error>; func save(_ note: Note); func delete(_ note: Note) }`
- [ ] `class CoreDataNoteRepository: NoteRepository` implementation
- [ ] `class MockNoteRepository: NoteRepository` for tests

### Milestone 3 — ViewModel with Combine
- [ ] `class NoteListViewModel: ObservableObject`
- [ ] `@Published var notes: [Note] = []`
- [ ] `@Published var searchQuery = ""` — debounce with `.debounce(for: 0.3, scheduler: RunLoop.main)`
- [ ] Combine pipeline: `$searchQuery.debounce.flatMap(repo.search).assign(to: &$notes)`

### Milestone 4 — Views
- [ ] `NoteListView` — List with swipe-to-delete, pin action, search bar
- [ ] `NoteDetailView` — TextEditor, tag picker, save on dismiss
- [ ] `TagFilterView` — horizontal scroll of tag chips
- [ ] Toolbar: sort button (by date / alphabetical / pinned first)

### Milestone 5 — Dependency Injection
- [ ] `protocol AppEnvironment { var noteRepo: NoteRepository { get } }`
- [ ] Pass environment via `.environment(appEnv)` in App entry point
- [ ] ViewModels receive environment via initializer

### Milestone 6 — Testing
- [ ] Unit tests: ViewModel with MockNoteRepository
- [ ] UI tests: XCUITest for critical flows (create/delete/pin)
