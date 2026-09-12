# Lecture 3 and 4 File Documentation

This document explains the purpose, usage, and algorithm behind each Python file
in this folder.

## Recursion examples

### `1.py` - Factorial

`Solution.factorial(n)` returns `n!`, the product of all positive integers up
to `n`. The base case returns `1` for `n <= 1`; larger values call the method
again with `n - 1`.

```python
Solution().factorial(5)  # 120
```

Complexity: `O(n)` time and `O(n)` call-stack space.

### `2.py` - Print from 1 to n

`Solution.printTillN(n)` prints the integers from `1` through `n` without a
loop. It makes the recursive call before printing, so the output is ascending.
The method returns `None` and does not print a newline.

```python
Solution().printTillN(4)  # prints 1234
```

Complexity: `O(n)` time and `O(n)` call-stack space.

### `3.py` - Sum of an array

`Solution.arraySum(arr)` recursively visits every item and returns the total.
The file also prints the sum of `[1, 2, 3, 4]` when it is run or imported.

```python
Solution().arraySum([1, 2, 3, 4])  # 10
```

Complexity: `O(n)` time and `O(n)` call-stack space.

### `4.py` and `5.py` - Fibonacci number

Both files implement `Solution.nthFibonacci(n)` using:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)`

```python
Solution().nthFibonacci(6)  # 8
```

Complexity: approximately `O(2^n)` time and `O(n)` call-stack space. These are
teaching examples; repeated subproblems make them slow for large `n`.

### `8.py` - Tower of Hanoi

`tower_of_hanoi(n, source, auxiliary, destination)` prints the moves required
to transfer `n` disks between rods. A larger disk is never placed on a smaller
disk. The file runs a three-disk example using rods `A`, `B`, and `C`.

Complexity: `O(2^n)` moves and `O(n)` call-stack space.

## Array and interview problems

### `6.py` - Running sum

`Solution.runningSum(nums)` replaces each item with the sum of itself and all
preceding items, then returns the same list.

```python
Solution().runningSum([1, 2, 3, 4])  # [1, 3, 6, 10]
```

Complexity: `O(n)` time and `O(1)` extra space.

### `7.py` - Add two numbers

This is an interactive example that asks for two numbers, converts them to
`float`, and prints their sum. The current source has naming errors: it assigns
the second input to `num1` instead of `num2`, then uses the undefined `num2`.
It needs those names corrected before it can run successfully.

### `9.py` - Largest array element

The file scans `[10, 25, 7, 89, 34]`, keeps the largest value seen, and prints
`89`.

Complexity: `O(n)` time and `O(1)` extra space.

### `10.py` - Maximum subarray

`Solution.maxSubArray(nums)` uses Kadane's algorithm to return the largest sum
of a contiguous, non-empty subarray.

```python
Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # 6
```

Complexity: `O(n)` time and `O(1)` extra space. The source needs
`from typing import List` before it can run.

### `11.py` - Maximum product subarray

`Solution.maxProduct(nums)` tracks both the smallest and largest product ending
at the current position. Both are needed because multiplying by a negative value
can turn the smallest product into the largest one.

```python
Solution().maxProduct([2, 3, -2, 4])  # 6
```

Complexity: `O(n)` time and `O(1)` extra space. The current source needs the
`List`, `min`, `max`, and `prodMax` name issues corrected before it can run.

### `12.py` - Majority element

`Solution.majorityElement(nums)` uses Boyer-Moore voting to find the value that
occurs more than half the time. It assumes a majority element exists and does
not perform a final verification pass.

```python
Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])  # 2
```

Complexity: `O(n)` time and `O(1)` extra space.

### `13.py` - Rotate array

`Solution.rotate(nums, k)` rotates `nums` to the right by `k` positions in
place. It reduces `k` modulo the list length, reverses the whole list, and then
reverses the two resulting sections. It returns `None`.

```python
values = [1, 2, 3, 4, 5]
Solution().rotate(values, 2)
print(values)  # [4, 5, 1, 2, 3]
```

Complexity: `O(n)` time and `O(1)` extra space.

### `14.py` - Two Sum

`Solution.twoSum(nums, target)` returns the indexes of two values whose sum is
`target`. A dictionary stores previously visited values, so each item is
checked once. It assumes a valid pair exists. The source needs
`from typing import List` before it can run.

```python
Solution().twoSum([2, 7, 11, 15], 9)  # [0, 1]
```

Complexity: `O(n)` average time and `O(n)` extra space.

### `15.py` - Sort Colors

`Solution.sortColors(nums)` sorts a list containing only `0`, `1`, and `2` in
place using the Dutch National Flag algorithm. It returns `None`.

```python
values = [2, 0, 2, 1, 1, 0]
Solution().sortColors(values)
print(values)  # [0, 0, 1, 1, 2, 2]
```

Complexity: `O(n)` time and `O(1)` extra space.

### `16.py` - Container With Most Water

`Solution.maxArea(height)` returns the greatest area formed by two heights and
the section of the x-axis between them. Two pointers start at opposite ends;
the pointer at the shorter height moves inward because moving the taller one
cannot improve the limiting height.

```python
Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])  # 49
```

Complexity: `O(n)` time and `O(1)` extra space.

## Calling the numbered modules

Most files expose a `Solution` class rather than accepting terminal input. Since
a filename that starts with a number cannot be imported with normal Python
syntax, use `import_module` in a Python shell:

```python
from importlib import import_module

rotate = import_module("13").Solution()
values = [1, 2, 3, 4, 5]
rotate.rotate(values, 2)
print(values)  # [4, 5, 1, 2, 3]
```

The class-based methods follow common online-judge conventions: they return a
value when specified, or mutate the input list and return `None` where noted.
