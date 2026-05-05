// PROJECT: SwiftUI Weather App | Open in Xcode, run on simulator
// Requires iOS 17+ / macOS 14+

import SwiftUI

// TODO 1: @main app entry point
//   @main
//   struct WeatherApp: App {
//       var body: some Scene {
//           WindowGroup { WeatherView() }
//       }
//   }

// TODO 2: WeatherData model
//   struct WeatherData: Decodable {
//       let city: String
//       let temperature: Double
//       let description: String
//       let humidity: Int
//       let windSpeed: Double
//   }

// TODO 3: WeatherService actor (thread-safe)
//   actor WeatherService {
//       private let apiKey = "YOUR_OPENWEATHERMAP_KEY"
//       private let baseURL = "https://api.openweathermap.org/data/2.5/weather"
//
//       func fetchWeather(for city: String) async throws -> WeatherData {
//           // TODO: build URL, URLSession.shared.data(from:), JSONDecoder().decode
//       }
//   }

// TODO 4: WeatherViewModel with @Observable (iOS 17)
//   @Observable
//   class WeatherViewModel {
//       var weatherData: WeatherData?
//       var isLoading = false
//       var errorMessage: String?
//       private let service = WeatherService()
//
//       func loadWeather(for city: String) async {
//           isLoading = true
//           defer { isLoading = false }
//           do {
//               weatherData = try await service.fetchWeather(for: city)
//           } catch {
//               errorMessage = error.localizedDescription
//           }
//       }
//   }

@main
struct WeatherAppStub: App {
    var body: some Scene {
        WindowGroup {
            Text("TODO: implement WeatherView")
        }
    }
}
