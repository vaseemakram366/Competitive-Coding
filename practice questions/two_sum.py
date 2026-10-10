# Two sum

def two_sum(nums, target):
    seen = {}
    for i , x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4],6))