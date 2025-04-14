n = (int(input("Enter a number")))
sum = 0
i = 1
while i < n:
    sum = sum+i
    i = i+1
print(sum)


#i = 0
#while i <= 0:
 #   print("INFINITE INFINITY INFINITEY")
 
num = int(input("Enter a number"))

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "Is an armstrong number")
else:
    print(num, "Is not a armstrong number")