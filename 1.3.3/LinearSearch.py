def find_min_linear(arr):
    minimum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]

    return minimum


arr = [2, 2, 2, 0, 1, 2]

print("Minimum:", find_min_linear(arr))