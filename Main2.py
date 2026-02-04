def poweroffour(n):
    if n <= 0:
        return 0
    if (n & (n-1)) == 0 and (n-1) % 3 == 0:
        return 1
    else:
        return 0
    
n = int(input("Enter a number : "))
if poweroffour(n) == 1:
    print(f"{n} | This is in the power of 4.")
else:
    print(f"{n} | This is not in the power of 4.")
    