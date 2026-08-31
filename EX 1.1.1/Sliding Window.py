def contains_duplicate(arr, k):
    window = set()

    for i, value in enumerate(arr):
        if value in window:
            return True

        window.add(value)

        if len(window) > k:
            window.remove(arr[i - k])

    return False


arr = [1, 0, 1, 1]
k = 1

if contains_duplicate(arr, k):
    print("True")
else:
    print("False")