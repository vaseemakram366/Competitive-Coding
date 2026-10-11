#  Search in Rotated Sorted Array II (with duplicates)

def search_ii(nums,target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True
        if nums[lo] == nums[mid] == nums[hi]:
            lo += 1
            hi -= 1
        elif nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False

print(search_ii([2,5,6,0,0,1,2],0))
print(search_ii([2,5,6,0,0,1,2],3))
print(search_ii([1,0,1,1,1],0))