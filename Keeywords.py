a = input("Enter a name: ")

for i in a:
    if (i == "a" or i == "A"):
        print("A is found")
        break
    else:
        print("A is not found")