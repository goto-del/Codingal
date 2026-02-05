def swap2(a,b):
    print(f"Before Swapping a = {a}, b = {b}.")
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print(f"After Swapping a = {a}, b = {b}.")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

swap2(a,b)