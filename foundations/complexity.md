# Complexity Analysis

## Big-O

Big-O describes an asymptotic upper-growth rate.

Common patterns:

### O(1)

```python
def first(values):
    return values[0]
```

### O(n)

```python
def total(values):
    result = 0
    for value in values:
        result += value
    return result
```

### O(n²)

```python
def all_pairs(values):
    for a in values:
        for b in values:
            pass
```

### O(log n)

Binary search is a classic example because each step roughly halves the
remaining search interval.

## Space complexity

Distinguish:

- input storage
- auxiliary memory
- recursion stack

When documenting an algorithm, state which one you are measuring.
