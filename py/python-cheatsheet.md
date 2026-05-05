# Python Cheat Sheet — Syntax & Algorithm Libraries

---

## 1. Basics

### Variables & Types
```python
x = 42          # int
y = 3.14        # float
s = "hello"     # str
b = True        # bool
n = None        # NoneType
type(x)         # <class 'int'>
isinstance(x, int)  # True
```

### Operators
```python
7 // 2    # 3    floor division
7 % 2     # 1    modulo
2 ** 10   # 1024 power
5 & 3     # 1    bitwise AND
5 | 3     # 7    bitwise OR
5 ^ 3     # 6    XOR
1 << 3    # 8    left shift
8 >> 2    # 2    right shift
```

### Conditionals
```python
if x > 0:
    print("pos")
elif x == 0:
    print("zero")
else:
    print("neg")

val = "yes" if x > 0 else "no"   # ternary
```

### Loops
```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i)

while x > 0:
    x -= 1

# for-else: else runs if no break occurred
for i in range(5):
    if i == 3: break
else:
    print("no break hit")
```

### I/O & Type Casting
```python
n = int(input("Enter: "))
print(f"val={n}")            # f-string
print(f"{n:.2f}")            # 2 decimal places
print("{:05d}".format(n))    # zero-padded

str(42)        # '42'
int("7")       # 7
float("3.14")  # 3.14
bin(10)        # '0b1010'
hex(255)       # '0xff'
ord('A')       # 65
chr(65)        # 'A'
```

### Useful Builtins
```python
abs(-5)           # 5
min(3, 1, 4)      # 1
max([3, 1, 4])    # 4
sum([1, 2, 3])    # 6
pow(2, 10, 1000)  # modular exponentiation: (2^10) % 1000
divmod(7, 2)      # (3, 1)
round(3.567, 2)   # 3.57
any([False, True])  # True
all([True, True])   # True
enumerate(lst)      # (index, value) pairs
zip(a, b)           # pairs elements from two iterables
map(fn, lst)        # lazy-apply fn to each element
filter(fn, lst)     # lazy-filter elements where fn is True
sorted(lst, key=fn, reverse=True)
```

---

## 2. Strings

### Slicing & Indexing
```python
s = "hello world"
s[0]        # 'h'
s[-1]       # 'd'
s[0:5]      # 'hello'
s[6:]       # 'world'
s[::-1]     # 'dlrow olleh'  (reverse)
len(s)      # 11
```

### Common Methods
```python
s.upper()           # 'HELLO WORLD'
s.lower()           # 'hello world'
s.strip()           # strip whitespace
s.lstrip("h")       # strip left
s.split(" ")        # ['hello', 'world']
" ".join(["a","b"]) # 'a b'
s.replace("l","L")  # 'heLLo worLd'
s.find("world")     # 6  (-1 if not found)
s.count("l")        # 3
s.startswith("he")  # True
s.endswith("ld")    # True
s.isdigit()         # False
s.isalpha()         # False
s.zfill(5)          # '00042'  (zero-pad)
```

### Formatting
```python
name, score = "Alice", 99.5
f"{name} scored {score:.1f}"    # f-string
f"{score:>10.2f}"               # right-align, width 10
f"{'hi':^10}"                   # center
f"{255:#010b}"                  # binary with prefix
```

---

## 3. Lists

### Creation & Access
```python
lst = [1, 2, 3, 4, 5]
lst[0]          # 1
lst[-1]         # 5
lst[1:3]        # [2, 3]
lst[::2]        # [1, 3, 5]  every other
lst[::-1]       # [5, 4, 3, 2, 1]  reversed
```

### Mutation
```python
lst.append(6)           # [1,2,3,4,5,6]
lst.insert(0, 0)        # insert at index
lst.extend([7, 8])      # concatenate
lst.pop()               # remove & return last
lst.pop(0)              # remove & return index 0
lst.remove(3)           # remove first occurrence of 3
lst.index(4)            # find index of value
lst.count(2)            # count occurrences
lst.reverse()           # in-place reverse
lst.sort()              # in-place sort
lst.sort(key=lambda x: -x)  # custom sort
lst.clear()             # empty the list
lst2 = lst.copy()       # shallow copy
```

### Useful Patterns
```python
lst = [0] * 5           # [0, 0, 0, 0, 0]
matrix = [[0]*3 for _ in range(3)]  # 3x3 grid (safe)
a, *b, c = [1,2,3,4,5]  # a=1, b=[2,3,4], c=5
x in lst                 # membership test O(n)
```

---

## 4. Tuples

```python
t = (1, 2, 3)
t[0]            # 1
a, b, c = t     # unpacking
t.count(2)      # 1
t.index(3)      # 2
# immutable — use as dict keys or fixed records
```

---

## 5. Dictionaries

### Creation & Access
```python
d = {"a": 1, "b": 2}
d["a"]              # 1
d.get("c", 0)       # 0  (default if missing)
d["c"] = 3          # insert/update
del d["a"]          # delete
"b" in d            # True
```

### Iteration
```python
d.keys()            # dict_keys
d.values()          # dict_values
d.items()           # (key, value) pairs

for k, v in d.items():
    print(k, v)
```

### Useful Methods
```python
d.pop("b", None)        # remove & return (safe)
d.setdefault("x", [])   # insert if missing
d.update({"y": 5})      # merge
d2 = {**d, "z": 6}      # merge via unpacking (Python 3.5+)
sorted(d.items(), key=lambda x: x[1])  # sort by value
```

---

## 6. Sets

```python
s = {1, 2, 3}
s.add(4)
s.discard(10)     # safe remove (no error)
s.remove(2)       # raises KeyError if missing

s1 | s2           # union
s1 & s2           # intersection
s1 - s2           # difference
s1 ^ s2           # symmetric difference
s1 <= s2          # is subset?
s1 >= s2          # is superset?

seen = set()
seen.add(x)
x in seen         # O(1) lookup
```

---

## 7. Functions

### Definitions & Arguments
```python
def greet(name, greeting="Hello"):   # default arg
    return f"{greeting}, {name}!"

def add(*args):           # variable positional
    return sum(args)

def info(**kwargs):       # variable keyword
    for k, v in kwargs.items():
        print(k, v)

def f(a, b, /, c, *, d):  # pos-only / kw-only after *
    pass
```

### Lambda, map, filter, reduce
```python
square = lambda x: x ** 2

list(map(lambda x: x*2, [1,2,3]))       # [2, 4, 6]
list(filter(lambda x: x%2==0, range(6)))# [0, 2, 4]

from functools import reduce
reduce(lambda a, b: a+b, [1,2,3,4])     # 10
```

### Closures & Decorators
```python
def outer(x):
    def inner(y):
        return x + y      # captures x
    return inner

add5 = outer(5)
add5(3)   # 8

import time
def timer(fn):
    def wrapper(*args, **kwargs):
        t = time.time()
        result = fn(*args, **kwargs)
        print(f"{time.time()-t:.4f}s")
        return result
    return wrapper

@timer
def slow():
    time.sleep(0.1)
```

### Generators
```python
def count_up(n):
    for i in range(n):
        yield i

gen = count_up(3)
next(gen)   # 0
next(gen)   # 1
list(gen)   # [2]

# generator expression (lazy)
squares = (x**2 for x in range(100))
```

---

## 8. List / Dict / Set Comprehensions

```python
# list comprehension
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
flat    = [x for row in matrix for x in row]

# dict comprehension
inv = {v: k for k, v in d.items()}
freq = {c: s.count(c) for c in set(s)}

# set comprehension
unique_lens = {len(w) for w in words}

# nested
grid = [(r, c) for r in range(3) for c in range(3)]
```

---

## 9. Sorting

```python
lst = [3, 1, 4, 1, 5]
lst.sort()                          # in-place
sorted(lst)                         # returns new list
sorted(lst, reverse=True)           # descending

# sort by key
words = ["banana", "fig", "apple"]
sorted(words, key=len)              # by length
sorted(words, key=lambda w: w[-1])  # by last char

# sort tuples / objects
pairs = [(1,'b'), (2,'a'), (1,'a')]
sorted(pairs)                       # lexicographic
sorted(pairs, key=lambda x: (x[0], x[1]))

# stable sort — equal keys keep original order
from operator import itemgetter, attrgetter
sorted(records, key=itemgetter(1))
```

---

## 10. Collections Module

### Counter
```python
from collections import Counter

c = Counter("abracadabra")
c.most_common(3)          # [('a',5),('b',2),('r',2)]
c["a"]                    # 5
c + Counter("aaa")        # add counts
c - Counter("aa")         # subtract (keeps positives)

# count elements in list
freq = Counter([1,1,2,3,2,1])
```

### defaultdict
```python
from collections import defaultdict

graph = defaultdict(list)
graph["A"].append("B")    # no KeyError on missing key

dd = defaultdict(int)
for ch in "hello":
    dd[ch] += 1           # auto-initializes to 0
```

### deque  *(O(1) append/pop from both ends)*
```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)          # [0,1,2,3]
dq.append(4)              # [0,1,2,3,4]
dq.popleft()              # 0
dq.pop()                  # 4
dq.rotate(1)              # [3,1,2]  rotate right

# use as a queue
queue = deque()
queue.append("a")         # enqueue
queue.popleft()           # dequeue
```

### heapq  *(min-heap)*
```python
import heapq

h = [3, 1, 4, 1, 5]
heapq.heapify(h)            # in-place O(n)
heapq.heappush(h, 2)        # push
heapq.heappop(h)            # pop smallest

# k smallest / largest
heapq.nsmallest(3, lst)
heapq.nlargest(3, lst)

# max-heap trick: negate values
max_heap = []
heapq.heappush(max_heap, -val)
top = -heapq.heappop(max_heap)

# priority queue with (priority, item)
pq = []
heapq.heappush(pq, (1, "low"))
heapq.heappush(pq, (0, "high"))
_, task = heapq.heappop(pq)   # "high"
```

### OrderedDict
```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a")       # move to end
od.popitem(last=False)    # pop from front (FIFO)
```

### namedtuple
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x, p.y    # 3, 4
```

---

## 11. itertools

```python
import itertools as it

it.count(10)              # 10, 11, 12, ...  (infinite)
it.cycle([1,2,3])         # 1,2,3,1,2,3,...  (infinite)
it.repeat(5, 3)           # 5, 5, 5

it.chain([1,2],[3,4])     # 1,2,3,4
it.chain.from_iterable([[1,2],[3,4]])  # same

it.islice(range(100), 5)  # 0,1,2,3,4  (lazy slice)

it.accumulate([1,2,3,4])        # 1,3,6,10  (prefix sums)
it.accumulate(lst, max)         # running max

# combinations / permutations
list(it.combinations([1,2,3], 2))   # [(1,2),(1,3),(2,3)]
list(it.permutations([1,2,3], 2))   # all ordered pairs
list(it.product([0,1], repeat=3))   # cartesian product (binary strings len 3)
list(it.combinations_with_replacement("AB", 2))  # [('A','A'),('A','B'),('B','B')]

# groupby (input must be sorted by key)
for key, group in it.groupby(sorted_lst, key=lambda x: x[0]):
    print(key, list(group))

it.takewhile(lambda x: x < 5, [1,3,6,2])  # 1,3
it.dropwhile(lambda x: x < 5, [1,3,6,2])  # 6,2
it.compress("ABCD", [1,0,1,0])             # A,C
```

---

## 12. math & Numeric

```python
import math

math.sqrt(16)       # 4.0
math.floor(3.7)     # 3
math.ceil(3.2)      # 4
math.log(8, 2)      # 3.0  (log base 2)
math.log2(8)        # 3.0
math.log10(100)     # 2.0
math.gcd(12, 8)     # 4
math.lcm(4, 6)      # 12  (Python 3.9+)
math.factorial(5)   # 120
math.comb(5, 2)     # 10  nCr
math.perm(5, 2)     # 20  nPr
math.inf            # float infinity
math.pi             # 3.14159...
math.isclose(0.1+0.2, 0.3)  # True (float comparison)

float('inf')        # infinity shorthand
float('-inf')       # negative infinity
```

---

## 13. Bisect  *(binary search on sorted list)*

```python
import bisect

a = [1, 3, 5, 7, 9]
bisect.bisect_left(a, 5)    # 2  (leftmost pos for 5)
bisect.bisect_right(a, 5)   # 3  (rightmost pos for 5)
bisect.insort_left(a, 4)    # insert 4 keeping sorted order

# find index of exact value
def find(a, x):
    i = bisect.bisect_left(a, x)
    return i if i < len(a) and a[i] == x else -1

# count elements in range [lo, hi]
def count_range(a, lo, hi):
    return bisect.bisect_right(a, hi) - bisect.bisect_left(a, lo)
```

---

## 14. OOP

```python
class Animal:
    species = "Unknown"         # class variable

    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age

    def speak(self):
        return f"{self.name} speaks"

    @classmethod
    def create(cls, name):      # factory
        return cls(name, 0)

    @staticmethod
    def breathes():             # no self/cls
        return True

    def __repr__(self):         # unambiguous repr
        return f"Animal({self.name!r}, {self.age})"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):    # enables sorting
        return self.age < other.age

    def __len__(self):
        return self.age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):            # override
        return "Woof!"

# dataclass (Python 3.7+) — auto __init__, __repr__, __eq__
from dataclasses import dataclass, field

@dataclass(order=True)
class Point:
    x: float
    y: float
    label: str = ""
    tags: list = field(default_factory=list)
```

---

## 15. Exception Handling

```python
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (ValueError, TypeError):
    pass
else:
    print("no exception")      # runs if no exception
finally:
    print("always runs")       # cleanup

# raise
raise ValueError("bad input")
raise                          # re-raise current exception

# custom exception
class AppError(Exception):
    def __init__(self, msg, code=0):
        super().__init__(msg)
        self.code = code

# context manager
with open("file.txt", "r") as f:
    data = f.read()            # file auto-closed

# suppress specific exceptions
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("maybe_missing.txt")
```

---

## 16. Useful Patterns for Algorithms

### Sliding Window
```python
def max_sum_window(arr, k):
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i-k]
        best = max(best, window)
    return best
```

### Two Pointers
```python
def two_sum_sorted(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target: return (l, r)
        elif s < target: l += 1
        else: r -= 1
```

### Prefix Sums
```python
def build_prefix(arr):
    pre = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        pre[i+1] = pre[i] + v
    return pre

# range sum [l, r] inclusive
def range_sum(pre, l, r):
    return pre[r+1] - pre[l]
```

### BFS / DFS templates
```python
from collections import deque

# BFS
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)

# DFS (iterative)
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

# DFS (recursive)
def dfs_rec(graph, node, visited=None):
    if visited is None: visited = set()
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            dfs_rec(graph, nbr, visited)
```

### Memoization / DP
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# manual memo
memo = {}
def fib2(n):
    if n in memo: return memo[n]
    if n < 2: return n
    memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

# cache_clear
fib.cache_clear()
```

### Backtracking template
```python
def backtrack(path, choices):
    if is_solution(path):
        results.append(path[:])
        return
    for choice in choices:
        if is_valid(choice, path):
            path.append(choice)
            backtrack(path, choices)
            path.pop()              # undo
```

---

## 17. sys & os

```python
import sys

sys.argv            # command-line arguments
sys.stdin.readline()
sys.setrecursionlimit(10**6)   # increase recursion limit
sys.maxsize                    # max int (~9.2e18)

import os

os.getcwd()
os.listdir(".")
os.path.exists("file.txt")
os.path.join("dir", "file.txt")
os.makedirs("dir/sub", exist_ok=True)
```

---

## 18. random

```python
import random

random.random()             # [0.0, 1.0)
random.randint(1, 10)       # 1..10 inclusive
random.choice([1,2,3])      # random element
random.choices([1,2,3], weights=[1,2,1], k=5)  # weighted
random.shuffle(lst)         # in-place
random.sample(lst, k=3)     # k unique elements
random.seed(42)             # reproducibility
```

---

## 19. String / Regex

```python
import re

re.match(r"\d+", "123abc")       # match at start
re.search(r"\d+", "abc123")      # search anywhere
re.findall(r"\d+", "a1b2c3")     # ['1','2','3']
re.sub(r"\s+", " ", text)        # replace
re.split(r"[,;]", "a,b;c")       # split on pattern

# compile for reuse
pat = re.compile(r"(\w+)@(\w+)")
m = pat.search(email)
m.group(0)    # full match
m.group(1)    # first capture group
```

---

## Quick Reference: Time Complexities

| Operation | List | Dict/Set | deque | heapq | bisect |
|-----------|------|----------|-------|-------|--------|
| Access by index | O(1) | — | O(n) | — | — |
| Search | O(n) | O(1) avg | O(n) | — | O(log n) |
| Insert (end) | O(1) amort | O(1) | O(1) | O(log n) | O(log n) search + O(n) insert |
| Insert (front) | O(n) | — | O(1) | — | — |
| Delete (end) | O(1) | O(1) | O(1) | — | — |
| Sort | O(n log n) | — | — | O(n) heapify | — |
| Min/Max | O(n) | — | — | O(1) peek | — |