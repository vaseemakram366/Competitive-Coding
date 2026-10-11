# Container With Most Water

def max_area(height):
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        area = min(height[l], height[r]) * (r - 1)
        best = max(best, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best
print(max_area([1,8,6,2,5,4,8,3,7]))
print(max_area([1,1]))

