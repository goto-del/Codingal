a = 2
b = 5
v = 8
l = 5
w = 10
z = (b+l) * v / a;
print("Value of (b+l) * v / a is ", z)

badge = 1
print("Ma'am have to give ", badge)


name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2 :
    print("Hello! Welcome.")
else:
    print("Goodbye!") 

if name == "Alex" and age >= 2 or name == "John" :
    print("Hello! Welcome.")
else:
    print("Goodbye!")      

print("Enter a number(Numerator): ")
numn = int(input())
print("Enter a number(Denominator): ")
numn = int(input())

if numn%numn==0:
    print("\n"+str(numn)+ " is divisible by "+str(numn))
else:
     print("\n"+str(numn)+ " is not divisible by "+str(numn))

mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40

sum = mean1*total_number


num2 = sum - ((wrong_number) - (correct_number))
print("sum - ((wrong_number) - (correct_number)): ",num2)


mean2=num2/total_number
print(mean2)