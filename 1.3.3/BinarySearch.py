def find_min_binary(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[right]:
            right = mid
        elif arr[mid] > arr[right]:
            left = mid + 1
        else:
            right -= 1

    return arr[left]


arr = [2, 2, 2, 0, 1, 2]

print("Minimum:", find_min_binary(arr))