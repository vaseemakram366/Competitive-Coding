# Sum of Array

class Solution:
    def arraySum(self, arr):
        def solve(i):
            if i == len(arr):
                return 0
            return arr[i] + solve(i + 1)

        return solve(0)

obj = Solution()
print(obj.arraySum([1, 2, 3, 4]))