# PROJECT: Sinatra REST API | gem install sinatra json && ruby app.rb
# Docs: https://sinatrarb.com/

# require 'sinatra'
# require 'json'

# TODO 1: Basic setup
#   set :port, 3000
#   set :bind, '0.0.0.0'
#   before { content_type :json }
#   configure { set :users, [] }

# TODO 2: GET /users — return all users as JSON
#   get '/users' do
#     settings.users.to_json
#   end

# TODO 3: GET /users/:id — return one or 404
#   get '/users/:id' do |id|
#     user = settings.users.find { |u| u[:id] == id.to_i }
#     halt 404, { error: "User not found" }.to_json unless user
#     user.to_json
#   end

# TODO 4: POST /users — parse JSON body and create
#   post '/users' do
#     data = JSON.parse(request.body.read, symbolize_names: true)
#     halt 422, { error: "name required" }.to_json unless data[:name]
#     user = { id: settings.users.size + 1, name: data[:name], email: data[:email] }
#     settings.users << user
#     status 201
#     user.to_json
#   end

# TODO 5: PUT /users/:id — update
# TODO 6: DELETE /users/:id — remove

# TODO 7: Add SQLite3 persistence with Sequel
#   require 'sequel'
#   DB = Sequel.sqlite('users.db')
#   DB.create_table?(:users) { primary_key :id; String :name, null: false; String :email, unique: true }

# TODO 8: Error handling middleware
#   error 404 do; { error: "Not found" }.to_json; end
#   error 500 do; { error: "Internal server error" }.to_json; end
