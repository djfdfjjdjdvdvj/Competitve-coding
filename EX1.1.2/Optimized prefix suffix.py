arr = [1, 2, 3, 4]
n = len(arr)

ans = [1] * n

prefix = 1
for i in range(n):
    ans[i] = prefix
    prefix *= arr[i]

suffix = 1
for i in range(n - 1, -1, -1):
    ans[i] *= suffix
    suffix *= arr[i]

print(ans)