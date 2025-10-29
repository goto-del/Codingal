def add(a, b):
    sum = a + b
    return sum
def subtract(a, b):
    difference = a - b
    return difference
def multiply(a, b):
    product = a * b
    return product
def divide(a, b):
    if b != 0:
        quotient = a / b
        return quotient
    else:
        return "Error! Division by zero."

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
if choice == "1":
    print(f"The sum is: {add(a, b)}")
elif choice == "2":
    print(f"The difference is: {subtract(a, b)}")
elif choice == "3":
    print(f"The product is: {multiply(a, b)}")
elif choice == "4":
    print(f"The quotient is: {divide(a, b)}")
else:
    print("Invalid input")