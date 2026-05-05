# TOPIC: Advanced Ruby | ruby 08_advanced.rb
# Docs: https://ruby-doc.org/

# TODO 1: Metaprogramming — dynamic method definition
#   class Person
#     ATTRS = [:name, :age, :email]
#     ATTRS.each do |attr|
#       define_method(attr) { instance_variable_get("@#{attr}") }
#       define_method("#{attr}=") { |v| instance_variable_set("@#{attr}", v) }
#     end
#   end
#   # Also: class_eval, instance_eval, send, public_send

# TODO 2: DSL patterns using method_missing
#   class FluentQuery
#     def method_missing(name, *args, &block)
#       if name.to_s.start_with?("find_by_")
#         field = name.to_s.sub("find_by_", "")
#         "SELECT * FROM table WHERE #{field} = #{args.first.inspect}"
#       else
#         super
#       end
#     end
#     def respond_to_missing?(name, include_private = false)
#       name.to_s.start_with?("find_by_") || super
#     end
#   end

# TODO 3: Module hooks — callbacks for include/extend/prepend/inherit
#   module Trackable
#     def self.included(base)
#       base.extend(ClassMethods)
#       base.instance_variable_set(:@tracked_classes, [])
#     end
#     module ClassMethods
#       def track(name); @tracked_classes << name; end
#     end
#   end

# TODO 4: Proc composition (Ruby 2.6+)
#   double    = ->(x) { x * 2 }
#   increment = ->(x) { x + 1 }
#   double_then_inc = double >> increment   # f >> g means g(f(x))
#   inc_then_double = double << increment   # f << g means f(g(x))
#   puts double_then_inc.call(5)  # => 11
#   puts inc_then_double.call(5)  # => 12

# TODO 5: Frozen objects and immutability
#   str = "hello".freeze
#   str << " world"  # => FrozenError!
#   dup_str = str.dup      # unfrozen duplicate
#   clone_str = str.clone  # frozen clone (preserves frozen state)
#   - frozen_string_literal: true at file top freezes all string literals

# TODO 6: BasicObject — blank slate for proxies
#   class Proxy < BasicObject
#     def initialize(target)
#       @target = target
#     end
#     def method_missing(name, *args, &block)
#       ::Kernel.puts "Calling #{name}"
#       @target.send(name, *args, &block)
#     end
#   end

# TODO 7: TracePoint — hook into Ruby VM events
#   trace = TracePoint.new(:call) do |tp|
#     puts "#{tp.defined_class}##{tp.method_id} called at #{tp.path}:#{tp.lineno}"
#   end
#   trace.enable { some_method_call }
#   # Events: :call, :return, :raise, :class, :end, :line, :b_call, :b_return

# TODO 8: Fiber Scheduler (Ruby 3.0+) — custom non-blocking I/O scheduler
#   # A Fiber::Scheduler allows gems like async to work transparently
#   # Implement: io_wait, process_wait, kernel_sleep, address_resolve
#   # Register with: Fiber.set_scheduler(MyScheduler.new)
#   # Fibers that call blocking operations will yield to the scheduler
