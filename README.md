# Data Structures & Algorithms

A practical, implementation-first repository for learning and practicing
Data Structures and Algorithms with Python.

---

## Learning Roadmap

```text
Foundations
   │
   ├── Complexity
   ├── Recursion
   └── Problem Solving
   │
   ▼
Linear Data Structures
   │
   ├── Arrays & Strings
   ├── Linked Lists
   ├── Stacks
   └── Queues
   │
   ▼
Hashing
   │
   ▼
Trees & Heaps
   │
   ▼
Graphs
   │
   ▼
Searching & Sorting
   │
   ▼
Algorithmic Paradigms
   │
   ├── Divide & Conquer
   ├── Greedy
   ├── Backtracking
   └── Dynamic Programming
   │
   ▼
Problem-Solving Patterns
   │
   ├── Two Pointers
   ├── Sliding Window
   ├── Prefix Sum
   ├── Hashing
   ├── Stack Patterns
   ├── Tree Traversal
   └── Graph Traversal
```

## Repository Structure

| Section | Focus |
|---|---|
| `00-foundations` | Complexity, recursion, problem-solving basics |
| `01-arrays-and-strings` | Arrays, strings, common operations |
| `02-linked-lists` | Singly and doubly linked lists |
| `03-stacks-and-queues` | Stack, queue, deque, priority queue concepts |
| `04-hashing` | Hash tables, sets, frequency counting |
| `05-trees-and-heaps` | Trees, BSTs, heaps, traversals |
| `06-graphs` | Graph representation and traversal |
| `07-searching` | Linear and binary search |
| `08-sorting` | Comparison and non-comparison sorting |
| `09-recursion` | Recursive problem solving |
| `10-divide-and-conquer` | Divide, solve, combine |
| `11-greedy` | Locally optimal choices |
| `12-backtracking` | Search with constraint-based undo |
| `13-dynamic-programming` | Memoization, tabulation, state design |
| `14-problem-solving` | Reusable interview/problem-solving patterns |
| `tests` | Automated checks |
| `progress` | Learning record |
| `resources` | References and study material |

## Complexity Cheat Sheet

| Structure / Algorithm | Typical Time | Extra Space |
|---|---:|---:|
| Array access | O(1) | O(1) |
| Linear search | O(n) | O(1) |
| Binary search | O(log n) | O(1) iterative |
| Hash lookup | O(1) average | O(n) |
| Stack push/pop | O(1) | O(n) |
| Queue enqueue/dequeue | O(1) | O(n) |
| Linked-list search | O(n) | O(1) |
| Merge sort | O(n log n) | O(n) |
| Quick sort | O(n log n) average | O(log n) average recursion |
| Heap insert | O(log n) | O(1) auxiliary |
| BFS / DFS | O(V + E) | O(V) |





## Running Tests

From the repository root:

```bash
python -m pytest
```

If pytest is not installed:

```bash
python -m pip install pytest
```

## Progress

See:

- `progress/roadmap.md`
- `progress/learning-log.md`

## Note

This is a learning repository. Implementations are intentionally kept readable
so that the underlying algorithm can be studied rather than hidden behind
large libraries.
