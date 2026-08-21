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
| `foundations` | Complexity, recursion, problem-solving basics |
| `arrays-and-strings` | Arrays, strings, common operations |
| `linked-lists` | Singly and doubly linked lists |
| `stacks-and-queues` | Stack, queue, deque, priority queue concepts |
| `hashing` | Hash tables, sets, frequency counting |
| `trees-and-heaps` | Trees, BSTs, heaps, traversals |
| `graphs` | Graph representation and traversal |
| `searching` | Linear and binary search |
| `sorting` | Comparison and non-comparison sorting |
| `recursion` | Recursive problem solving |
| `divide-and-conquer` | Divide, solve, combine |
| `greedy` | Locally optimal choices |
| `backtracking` | Search with constraint-based undo |
| `dynamic-programming` | Memoization, tabulation, state design |
| `problem-solving` | Reusable interview/problem-solving patterns |
| `tests` | Automated checks |


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

