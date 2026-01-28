def numberofbits(n):
    ones = 0
    zeros = 0
    while n:
        if n & 1 == 1:
            ones = ones + 1
        else:
            zeros = zeros + 1
        n = n >> 1
    print(f"The number of Zero's are {zeros} and the number of One's are {ones}.")
n = int(input("Enter any number : "))

numberofbits(n)