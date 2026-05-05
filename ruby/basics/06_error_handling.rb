# TOPIC: Error Handling | ruby 06_error_handling.rb

# TODO 1: begin/rescue/ensure/else — rescue StandardError => e, e.message, e.backtrace
# TODO 2: Custom exceptions — class AppError < StandardError; class DBError < AppError
# TODO 3: retry — inside rescue block, retry up to 3 times with exponential backoff
# TODO 4: raise vs fail — both work, raise preferred; raise with class, message, or instance
# TODO 5: rescue in method body — no begin needed: def risky; ...; rescue => e; end
# TODO 6: Multiple rescue clauses — rescue TypeError, ArgumentError => e
# TODO 7: ensure — always runs (like finally), use for cleanup (file close, unlock)
# TODO 8: Exception hierarchy — Exception > StandardError > RuntimeError; don't rescue Exception
