def checkifequal(num1, num2):
    if (num1 ^ num2) != 0:
        print("Numbers are not equal")
    else:
        print("Numbers are equal")

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

checkifequal(num1, num2)