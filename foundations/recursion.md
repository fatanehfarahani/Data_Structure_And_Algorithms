# Recursion

A recursive algorithm calls itself on a smaller version of the problem.

A recursive solution normally needs:

1. A base case
2. A recursive case
3. Progress toward the base case

Example:

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

Questions to ask:

- What is the base case?
- What gets smaller?
- How many recursive calls occur?
- What is the recursion depth?
