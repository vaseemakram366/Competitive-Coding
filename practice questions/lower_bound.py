# Lower Bound

def lower_bound(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo
a = [1,2,4,4,6,8]
print(lower_bound(a, 4))
print(lower_bound(a, 5))
print(lower_bound(a,10))