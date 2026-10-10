# Count Elements with maximum frequency

from collections import Counter

def max_freq_elements(nums):
    freq = Counter(nums)
    mx = max(freq.values())
    return sum(f for f in freq.values() if f == mx)
print(max_freq_elements([1,2,2,3,1,4]))
print(max_freq_elements([1,2,3,4,5]))       