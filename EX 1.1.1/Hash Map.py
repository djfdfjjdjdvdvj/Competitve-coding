def contains_duplicate(arr, k):
    last_index = {}

    for i, value in enumerate(arr):
        if value in last_index:
            if i - last_index[value] <= k:
                return True
        last_index[value] = i

    return False


arr = [1, 2, 3, 1]
n = 4
k = 3

if contains_duplicate(arr, k):
    print("True")
else:
    print("False")