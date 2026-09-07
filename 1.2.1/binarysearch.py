def integer_sqrt(x):
    if x < 2:
        return x

    left = 1
    right = x
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= x:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


x = int(input("Enter a non-negative integer: "))
print("Integer square root:", integer_sqrt(x))