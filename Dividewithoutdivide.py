a = int(input("Enter any number : "))
b = int(input("Enter another number : "))

count = 0
while a >= b:
    a = a - b
    count = count+1
    

print(f"Quotient is {count}.")
print(f"Remainder is {a}.")