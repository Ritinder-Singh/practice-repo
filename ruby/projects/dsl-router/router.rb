# PROJECT: DSL Router using method_missing + define_method (Exclusive)
# Build a Rack-compatible router with a Rails-like DSL:
#
# router = Router.new do
#   get "/users", to: "users#index"
#   post "/users", to: "users#create"
#   resources :posts  # generates 7 RESTful routes
# end
#
# result = router.call({ "REQUEST_METHOD" => "GET", "PATH_INFO" => "/users" })

# TODO 1: Router class with instance_eval block
#   class Router
#     def initialize(&block)
#       @routes = {}  # { [method, path] => handler_string }
#       instance_eval(&block) if block_given?
#     end
#   end

# TODO 2: HTTP verb methods — get/post/put/patch/delete
#   def get(path, to:)
#     @routes[["GET", path]] = to
#   end
#   # repeat for post, put, patch, delete

# TODO 3: resources helper — generates 7 RESTful routes
#   def resources(name)
#     base = "/#{name}"
#     get    base,               to: "#{name}#index"
#     get    "#{base}/new",      to: "#{name}#new"
#     post   base,               to: "#{name}#create"
#     get    "#{base}/:id",      to: "#{name}#show"
#     get    "#{base}/:id/edit", to: "#{name}#edit"
#     put    "#{base}/:id",      to: "#{name}#update"
#     delete "#{base}/:id",      to: "#{name}#destroy"
#   end

# TODO 4: Path parameter matching — /users/:id matches /users/42
#   def match_path(pattern, path)
#     # Convert pattern to regex: "/users/:id" → /^\/users\/(?<id>[^\/]+)$/
#     # Return [true, {id: "42"}] or [false, {}]
#   end

# TODO 5: call(env) — Rack interface
#   def call(env)
#     method = env["REQUEST_METHOD"]
#     path   = env["PATH_INFO"]
#     @routes.each do |(route_method, route_path), handler|
#       matched, params = match_path(route_path, path)
#       if route_method == method && matched
#         controller_name, action = handler.split("#")
#         return dispatch(controller_name, action, params)
#       end
#     end
#     [404, {"Content-Type" => "text/plain"}, ["Not Found"]]
#   end

# TODO 6: Controller dispatch — find class, call action
#   def dispatch(controller, action, params)
#     klass = Object.const_get("#{controller.capitalize}Controller")
#     instance = klass.new(params)
#     body = instance.public_send(action)
#     [200, {"Content-Type" => "application/json"}, [body.to_json]]
#   end

# TODO 7: Base Controller class
#   class Controller
#     attr_reader :params
#     def initialize(params) = @params = params
#     def render(data) = data  # simple return, dispatch converts to JSON
#   end
