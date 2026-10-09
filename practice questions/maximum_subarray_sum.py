# Maximum Subarray Sum(Kadane's Algorithm)

def max_subarray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur+x)
        best = max(best, cur)
    return best
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([-3,-1,-2]))