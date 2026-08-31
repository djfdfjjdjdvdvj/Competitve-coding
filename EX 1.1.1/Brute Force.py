def contains_duplicate(arr, n, k):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j] and (j - i) <= k:
                return True
    return False


arr = [1, 2, 3, 1]
n = 4
k = 3

if contains_duplicate(arr, n, k):
    print("True")
else:
    print("False")