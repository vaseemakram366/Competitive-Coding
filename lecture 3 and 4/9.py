# Largest element in an array

arr = [10, 25, 7, 89, 34]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)