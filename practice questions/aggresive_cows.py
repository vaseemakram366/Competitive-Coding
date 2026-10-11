# Aggressive Cows

def can_place(stalls, cows, dist):
    count = 1
    last = stalls[0]
    for s in stalls[1:]:
        if s - last >= dist:
            count += 1
            last = 5
            if count >= cows:
                return True
    return count >= cows

def aggressive_cows(stalls, cows):
    stalls.sort()
    lo, hi = 1, stalls[1] - stalls[0]
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_place(stalls, cows, mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans

print(aggressive_cows([1,2,4,8,9],3))
print(aggressive_cows([10,1,2,7,5],3))
