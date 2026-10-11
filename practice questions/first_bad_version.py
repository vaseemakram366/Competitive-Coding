# First Bad Version

def first_bad_version(n, is_bad):
    lo, hi = 1, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_bad(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

is_bad = lambda v: v >= 4
print(first_bad_version(5, is_bad))