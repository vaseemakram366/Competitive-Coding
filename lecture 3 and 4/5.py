# Nth Fibonacci number

class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1
# recursion
        return self.nthFibonacci(n - 1) + self.nthFibonacci(n - 2)