# Lecture 3 and 4: Recursion and Arrays

This folder contains Python practice programs from lectures 3 and 4. The
examples introduce recursion and build toward common array and coding
interview problems.

## Contents

| File | Topic | Main idea |
| --- | --- | --- |
| `1.py` | Factorial | Recursive multiplication from `n` down to `1` |
| `2.py` | Print `1` to `n` | Recursion without using a loop |
| `3.py` | Sum of an array | Recursive traversal of an array |
| `4.py` | Nth Fibonacci number | Recursive Fibonacci sequence |
| `5.py` | Nth Fibonacci number | Another recursive Fibonacci implementation |
| `6.py` | Running sum | In-place prefix sums |
| `7.py` | Add two numbers | Input, type conversion, and arithmetic |
| `8.py` | Tower of Hanoi | Recursive movement of disks between rods |
| `9.py` | Largest array element | Linear scan for the maximum value |
| `10.py` | Maximum subarray | Kadane's algorithm |
| `11.py` | Maximum product subarray | Track the current minimum and maximum products |
| `12.py` | Majority element | Boyer-Moore voting algorithm |
| `13.py` | Rotate array | In-place rotation using array reversal |
| `14.py` | Two Sum | Hash map lookup for a target pair |
| `15.py` | Sort Colors | Dutch National Flag algorithm for in-place sorting |
| `16.py` | Container With Most Water | Two-pointer search for the maximum area |

## Requirements

- Python 3.9 or newer
- No third-party packages are required

## Running the examples

Open a terminal in this directory and run an individual script:

```text
python 1.py
```

Some files only define a `Solution` class, so they are intended to be called
from a judge or a Python shell. For example:

```python
from importlib import import_module

solution = import_module("3").Solution()
print(solution.arraySum([1, 2, 3, 4]))
```

Scripts that contain `input()` will wait for values in the terminal. Files
with direct `print()` calls display their sample result when run.

## Notes

- `4.py` and `5.py` demonstrate the same Fibonacci problem in two files.
- The recursive Fibonacci examples are easy to understand but become slow for
	larger values because they repeat work.
- `15.py` sorts the input list in place and does not return a new list.
- `16.py` returns the maximum container area calculated from the input heights.
- `7.py`, `10.py`, `11.py`, and `14.py` currently need small fixes before they
	can run directly: undefined variable names or missing `List` imports are
	present in the source.
- These examples are educational and favor clarity over production-ready
	input validation and optimization.
