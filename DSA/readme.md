# Data Structures and Algorithms Practice

This folder contains data structures and algorithms practice completed as part of the Python apprenticeship.

The goal of this work is not just interview preparation. It is also to build a stronger understanding of how data is organized, how operations affect performance, and how to reason clearly about correctness and efficiency.

## Topics covered so far

### 1. Stack
A stack implementation using a Python list.

**Concepts practiced:**
- LIFO behavior
- `push`, `pop`, `peek`, `is_empty`
- Error handling on empty pop
- Testing stack behavior with pytest

### 2. Queue
A queue implementation using `collections.deque`.

**Concepts practiced:**
- FIFO behavior
- `enqueue`, `dequeue`, `peek`, `is_empty`
- Why `deque` is preferred over list front-removal
- Testing queue behavior with pytest

### 3. Linear algorithms
Simple algorithms that scan through a list.

**Concepts practiced:**
- `find_max`
- `linear_search`
- `count_occurrences`
- O(n) reasoning
- Empty-list and not-found edge cases

### 4. Array algorithms
Applied list/array problems implemented without relying on built-in shortcuts.

**Concepts practiced:**
- Reverse a list in place
- Find the second largest distinct value
- Move zeroes to the end in place
- Two-pointer thinking
- In-place vs extra-space tradeoffs

### 5. Singly linked list
A first linked list implementation using nodes and `next` references.

**Concepts practiced:**
- Node-based data structures
- `insert_at_head`
- `append`
- `find`
- `delete_first`
- Converting a linked list to a Python list for testing
- Pointer rewiring and deletion logic

## Why this folder matters

This folder shows the beginning of real computer science skill-building in the apprenticeship. The focus is on understanding what the structures do, how to implement them, and what their performance tradeoffs are.

## Testing

Run all DSA tests from this folder with:

```bash
python -m pytest -v
```

You can also run a single test file, for example:

```bash
python -m pytest test_ds_stack.py -v
python -m pytest test_ds_queue.py -v
python -m pytest test_ds_linear.py -v
python -m pytest test_ds_array_algorithms.py -v
python -m pytest test_ds_linked_list.py -v
```

## Learning priorities in this folder

The priorities here are:

- correctness first
- readable code
- strong edge-case handling
- Big-O awareness at a beginner-friendly level
- repeated practice through implementation and testing

## Future additions

Likely next topics include:

- dictionaries and hash-map style problems
- sorting fundamentals
- searching patterns
- recursion basics
- trees and graphs later on