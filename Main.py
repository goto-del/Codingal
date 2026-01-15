num = int(input("Enter a number : "))
original = num
reversed = 0
while num > 0:
    digit = num%10
    reversed = reversed*10+digit
    num = num // 10

if original == reversed:
    print(f"{original} is a palindromic number.")
else:
    print(f"{original} is not a palindromic number.")