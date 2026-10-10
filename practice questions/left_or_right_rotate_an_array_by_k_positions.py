# Left / Right Rotate an Array by k positions

def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return
    k %= n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

def rotate_left(nums, k):
    n = len(nums)
    if n == 0:
        return
    k %= n
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    reverse(nums, 0, n - 1)

a = [1,2,3,4,5]
rotate_right(a, 2)
print(a)

b = [1,2,3,4,5]
rotate_left(b,2)
print(b)