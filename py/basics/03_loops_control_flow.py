# =============================================================================
# Python — Loops & Control Flow
# =============================================================================
# Topics: for/while loops, comprehensions, iterators, generators,
#         break/continue/else on loops, match statement (3.10+).
# Run: python 03_loops_control_flow.py
# =============================================================================

# TODO 1: for loop with enumerate and zip
#   Given names = ["Alice", "Bob"] and scores = [95, 87]:
#   Print: "1. Alice: 95" using enumerate(names, start=1) and zip

# TODO 2: List, dict, set comprehensions
#   TODO 2a: squares = [x² for x in range(10) if x % 2 == 0]
#   TODO 2b: word_lengths = {word: len(word) for word in ["hello", "world"]}
#   TODO 2c: unique_chars = {c for c in "hello world" if c != " "}
#   TODO 2d: flatten = [x for row in [[1,2],[3,4],[5,6]] for x in row]

# TODO 3: while loop with else clause
#   Implement binary search using while/else:
#   - If found: print "Found at index N"
#   - else clause runs only if loop completes without break (not found)
#
# def binary_search(nums: list, target: int) -> int:
#     lo, hi = 0, len(nums) - 1
#     while lo <= hi:
#         pass
#     else:
#         return -1

# TODO 4: Generators
#   TODO 4a: Write fibonacci() generator (infinite sequence)
#   TODO 4b: Write read_large_file(path) generator (yields lines, memory-efficient)
#   TODO 4c: Use yield from to flatten a nested list
#
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# TODO 5: Custom Iterator class
#   Implement a Range class (like Python's range()) using __iter__ and __next__:
#
# class MyRange:
#     def __init__(self, start, stop, step=1):
#         pass
#     def __iter__(self):
#         return self
#     def __next__(self):
#         pass

# TODO 6: match statement (Python 3.10+)
#   Implement a command dispatcher using structural pattern matching:
#   parse_command("move north") → ("move", "north")
#   parse_command("attack goblin with sword") → ("attack", "goblin", "sword")
#
# def handle_command(command: str) -> str:
#     parts = command.split()
#     match parts:
#         case ["quit"]:
#             return "Quitting..."
#         case ["go", direction]:
#             return f"Going {direction}"
#         case ["attack", enemy, "with", weapon]:
#             return f"Attacking {enemy} with {weapon}"
#         case _:
#             return "Unknown command"

# TODO 7: itertools
#   Practice: chain, islice, product, combinations, permutations, groupby
#   Example: find all 2-element combinations of [1,2,3,4] where sum > 4
#   import itertools
