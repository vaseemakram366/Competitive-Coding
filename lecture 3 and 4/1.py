# factorial

class Solution:
    def factorial(self, n: int) -> int:
        # code here
        if n <= 1:
            return 1
        else:
            return n * self.factorial(n - 1)