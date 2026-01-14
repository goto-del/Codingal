num = int(input("Enter a number : "))
d = len(str(num))
result = 0
temp = num
while temp > 0:
    digit = temp%10
    digit = digit ** d
    result = result + digit
    temp = temp // 10
    

if result == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")