arr = [1, 2, 3, 4]
n = len(arr)

ans = [1] * n

for i in range(n):
    for j in range(n):
        if i != j:
            ans[i] *= arr[j]

print(ans)