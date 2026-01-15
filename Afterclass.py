def findlcm(a,b):
    greater = max(a,b)
    while True:
        if greater%a == 0 and greater %b == 0:
            return greater
        greater = greater+1

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

print(f"The LCM of {a} and {b} is {findlcm(a,b)}")
