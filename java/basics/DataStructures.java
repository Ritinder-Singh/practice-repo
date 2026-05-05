package basics;
// TOPIC: Data Structures | javac DataStructures.java && java basics.DataStructures
import java.util.*;
import java.util.stream.*;

public class DataStructures {
    public static void main(String[] args) {
        // TODO 1: ArrayList vs LinkedList — benchmark add/get/remove
        //   - ArrayList<Integer>: O(1) amortized add-end, O(1) get(i), O(n) add/remove-middle
        //   - LinkedList<Integer>: O(1) add/remove-ends, O(n) get(i) — no random access
        //   - Benchmark: time 100,000 add-to-front operations for each, print elapsed ms
        //   - Benchmark: time 10,000 get(random index) operations for each
        //   - Use System.nanoTime() for timing

        // TODO 2: HashMap — core operations
        //   - Map<String, Integer> wordCount = new HashMap<>();
        //   - put(k,v), get(k), getOrDefault(k, 0), containsKey(k), remove(k)
        //   - computeIfAbsent("key", k -> new ArrayList<>())  // safe initialization
        //   - merge(k, 1, Integer::sum)  // clean frequency counting
        //   - Iterate: entrySet(), keySet(), values()
        //   - Initial capacity and load factor: new HashMap<>(16, 0.75f)

        // TODO 3: HashSet vs TreeSet
        //   - HashSet: O(1) add/contains/remove, no order
        //   - TreeSet: O(log n), sorted by natural order or Comparator
        //   - Deduplication: new HashSet<>(list) removes duplicates
        //   - Set union: setA.addAll(setB)
        //   - Set intersection: setA.retainAll(setB)
        //   - Set difference: setA.removeAll(setB)
        //   - TreeSet extras: first(), last(), headSet(to), tailSet(from), subSet(from, to)

        // TODO 4: Stack & Deque — ArrayDeque as stack and queue
        //   - As stack (LIFO): Deque<Integer> stack = new ArrayDeque<>();
        //     stack.push(1); stack.pop(); stack.peek();
        //   - As queue (FIFO): Deque<Integer> queue = new ArrayDeque<>();
        //     queue.offer(1); queue.poll(); queue.peek();
        //   - Note: ArrayDeque is faster than Stack class (no synchronization overhead)
        //   - Demonstrate balanced parentheses checker using stack

        // TODO 5: PriorityQueue — heaps
        //   - Min-heap (default): PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        //     offer/add elements, poll() always returns smallest
        //   - Max-heap: PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        //   - Custom object heap: PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[1]-b[1]);
        //   - Use case: find K largest elements in O(n log k)

        // TODO 6: LinkedHashMap — LRU cache
        //   - class LRUCache<K,V> extends LinkedHashMap<K,V> {
        //       private final int capacity;
        //       LRUCache(int capacity) { super(capacity, 0.75f, true); this.capacity = capacity; }
        //       @Override protected boolean removeEldestEntry(Map.Entry eldest) {
        //           return size() > capacity;
        //       }
        //     }
        //   - accessOrder=true in constructor keeps recently accessed entries at tail
        //   - Demonstrate: cache capacity 3, access pattern, verify eviction

        // TODO 7: TreeMap — range queries
        //   - TreeMap<Integer, String> tm = new TreeMap<>();
        //   - floorKey(k): largest key <= k
        //   - ceilingKey(k): smallest key >= k
        //   - lowerKey(k), higherKey(k): strictly less/greater
        //   - subMap(from, fromInclusive, to, toInclusive): range view
        //   - headMap(to), tailMap(from)
        //   - firstKey(), lastKey(), pollFirstEntry(), pollLastEntry()

        // TODO 8: Implement generic Stack<T> from scratch
        //   - class Stack<T> {
        //       private Object[] data;
        //       private int size;
        //       private static final int INITIAL_CAPACITY = 16;
        //       Stack() { data = new Object[INITIAL_CAPACITY]; }
        //       void push(T item): if full, resize (double capacity with Arrays.copyOf)
        //       T pop(): if empty throw EmptyStackException; return (T) data[--size]; data[size]=null;
        //       T peek(): return (T) data[size-1];
        //       boolean isEmpty(): return size == 0;
        //       int size(): return size;
        //       private void resize(int newCapacity): data = Arrays.copyOf(data, newCapacity);
        //     }
        //   - Test with String, Integer; verify resizing by pushing 20 elements
    }
}
