def findgcd(a,b):
    gcd = 1
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            gcd = i
    return gcd

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

print(f"The GCD of {a} and {b} is {findgcd(a,b)}")

