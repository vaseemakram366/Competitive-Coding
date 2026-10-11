# Upper Bound

def upper_bound(arr):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo

a = [1,2,4,4,6,8]
print(upper_bound(a,4))
print(upper_bound(a,8))
print(upper_bound(a,0))