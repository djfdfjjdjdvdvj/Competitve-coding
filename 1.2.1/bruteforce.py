def integer_sqrt(x):
    i = 0

    while i * i <= x:
        i += 1

    return i - 1


x = int(input("Enter a non-negative integer: "))
print("Integer square root:", integer_sqrt(x))