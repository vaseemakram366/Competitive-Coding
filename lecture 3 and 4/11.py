# Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = nums[0]
        curMax = nums[0]
        prodMax = nums[0]
        for i in range(1, len(nums)):
            prevMin = currMin
            prevMax = currMax
            currMin = Min(nums[i], nums[i]*prevMin,nums[i]*prevMax)
            currMax = Max(nums[i], nums[i]*prevMin,nums[i]*prevMax)
            prodMax = max(proMax, currMax)
        return prodMax