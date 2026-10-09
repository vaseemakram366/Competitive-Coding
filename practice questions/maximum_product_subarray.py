# Maximum product subarray(kadane based)

def max_product(nums):
    cur_max = cur_min = best = nums[0]
    for x in nums[1:]:
        if x < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(x, cur_max * x)
        cur_min = min(x, cur_min * x)
        best = max(best, cur_max)
    return best 

print(max_product([2,3,-2,4]))
print(max_product([-2,0,-1]))
print(max_product([-2,3,-4]))