def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Enter a number to compute its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")
    
