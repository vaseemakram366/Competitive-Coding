# Koko Eating Bananas

def min_eating_speed(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum((p + mid - 1) // mid for p in piles)
        if hours <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo

print(min_eating_speed([3,6,7,11],8))
print(min_eating_speed([30,11,23,4,20],5))