num = int(input("Enter any number : "))

if num <= 1:
    print(f"{num} is a negative number so it cannot be considered prime or non-prime.")
else:
    isprime = True
    for i in range(2, num):
        if num % i == 0:
            isprime = False
            break
    if isprime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number")