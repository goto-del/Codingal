def poweroftwo(n):
    if n == 0:
        return 0
    if (n & (n-1) == 0):
        return 1
    return 0

n = int(input("Enter a number : "))
if poweroftwo(n) == 1:
    print(f"{n} | This number is a power of 2.")
else:
    print(f"{n} | This number is not the power of 2.")