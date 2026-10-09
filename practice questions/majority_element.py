# Majority Element(Moore's voting algorithm)
def majority_element(nums):
    cand, count = None, 0
    for x in nums:
        if count == 0:
            cand = x
        count += 1 if x == cand else -1
    return  cand

print(majority_element([2,2,1,1,1,2,2]))
print(majority_element([3,2,3]))