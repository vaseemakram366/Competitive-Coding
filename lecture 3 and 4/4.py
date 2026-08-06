# Nth Fibonacci Number

class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Recursive case
        return self.nthFibonacci(n - 1) + self.nthFibonacci(n - 2)