def swap(a,b):
    print(f"Before Swapping a = {a}, b = {b} ")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After Swapping a = {a}, b = {b} ")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

swap(a,b)