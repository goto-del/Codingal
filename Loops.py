n = int(input("Enter the number whose sum you want to find: "))
sum = 0


for i in range(1 , n+1):
    sum = sum+i
    print("\nSum", sum)


string = (input("Enter your own string: "))

string2 = ('')
for i in string:
    string2 = i + string2


print("Original string: ",string)
print("Reversed string: ",string2)

n = int(input("Enter the value of n: "))
print("numbers from {0} to {1} ". format(n,1))

for i in range(n,0,-1):
    print(i)