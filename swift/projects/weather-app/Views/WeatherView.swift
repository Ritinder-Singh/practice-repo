import SwiftUI

// PROJECT: WeatherView — main weather display screen

// TODO 1: @State and @Environment setup
//   struct WeatherView: View {
//       @State private var viewModel = WeatherViewModel()
//       @State private var cityInput = ""
//   }

// TODO 2: Main layout
//   var body: some View {
//       NavigationStack {
//           VStack(spacing: 20) {
//               searchBar        // TODO: TextField + Button
//               weatherDisplay   // TODO: conditional based on viewModel.weatherData
//           }
//           .navigationTitle("Weather")
//       }
//   }

// TODO 3: Search bar component
//   private var searchBar: some View {
//       HStack {
//           TextField("Enter city name...", text: $cityInput)
//               .textFieldStyle(.roundedBorder)
//               .onSubmit { Task { await viewModel.loadWeather(for: cityInput) } }
//           Button("Search") { Task { await viewModel.loadWeather(for: cityInput) } }
//               .buttonStyle(.borderedProminent)
//       }
//       .padding()
//   }

// TODO 4: Weather display — show temperature, description, humidity, wind
//   private var weatherDisplay: some View {
//       Group {
//           if viewModel.isLoading {
//               ProgressView("Fetching weather...")
//           } else if let data = viewModel.weatherData {
//               WeatherCardView(data: data)  // TODO: separate component
//           } else if let error = viewModel.errorMessage {
//               Text(error).foregroundStyle(.red)
//           } else {
//               Text("Search for a city above").foregroundStyle(.secondary)
//           }
//       }
//   }

// TODO 5: WeatherCardView — styled card showing weather info
//   struct WeatherCardView: View {
//       let data: WeatherData
//       var body: some View {
//           VStack(spacing: 12) {
//               Text(data.city).font(.largeTitle.bold())
//               Text("\(Int(data.temperature))°C").font(.system(size: 72, weight: .thin))
//               Text(data.description.capitalized).font(.title2)
//               HStack(spacing: 40) {
//                   Label("\(data.humidity)%", systemImage: "humidity")
//                   Label("\(Int(data.windSpeed)) km/h", systemImage: "wind")
//               }
//           }
//           .padding()
//           .background(.regularMaterial, in: RoundedRectangle(cornerRadius: 20))
//           .padding()
//       }
//   }

struct WeatherView: View {
    var body: some View {
        Text("TODO: implement weather view")
    }
}
