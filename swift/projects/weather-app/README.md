# Weather App (SwiftUI + async/await)

## Setup
1. Create a new SwiftUI project in Xcode (File > New > Project > App).
2. Set minimum deployment target to iOS 17.
3. Replace the generated files with the stubs in this folder.
4. Add `WeatherView.swift` inside a `Views/` group.

## TODOs

### WeatherService (actor)
- TODO: Define `actor WeatherService` to serialize network access.
- TODO: `func fetchWeather(city: String) async throws -> WeatherData`
  - Build URLRequest from OpenWeatherMap (or mock) endpoint.
  - Decode JSON into a `WeatherData` Codable struct.
  - Throw `WeatherError.cityNotFound` / `.networkFailure` as appropriate.

### WeatherView
- TODO: `@State private var city: String = ""`
- TODO: `@State private var weather: WeatherData?`
- TODO: `@StateObject var viewModel: WeatherViewModel` (or use the actor directly with Task)
- TODO: Build a VStack with TextField for city name, Button("Search"), and conditional result display.
- TODO: Show temperature, condition icon (SF Symbol or AsyncImage), and humidity.

### LocationManager (CoreLocation)
- TODO: Create `class LocationManager: NSObject, CLLocationManagerDelegate, ObservableObject`.
- TODO: `@Published var location: CLLocation?`
- TODO: Request `whenInUse` authorization; implement `didUpdateLocations`.
- TODO: Reverse-geocode to get city name, feed into WeatherService.

### Error Handling
- TODO: Show `.alert` modifier on WeatherView bound to an optional error string.
- TODO: Map `WeatherError` cases to user-readable messages.

### Unit Tests
- TODO: Create `WeatherServiceTests.swift` in the test target.
- TODO: Define `MockWeatherService` conforming to a `WeatherServiceProtocol`.
- TODO: Test that `WeatherViewModel` exposes correct state on success and failure.
