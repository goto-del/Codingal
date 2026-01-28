def setbitornot(num, p):
    if num & (1 << (p-1)):
        print("set\n")
    else:
        print("Not set\n")
num = int(input("Enter a number : "))
p = int(input("Enter the position : "))
setbitornot(num , p)