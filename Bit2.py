def oddocurring(l):
    result = 0
    for i in l:
        result = result ^ i
    return result

l = []
n = int(input("Enter the number of elements in the list : "))
for i in range(n):
    element = int(input("Enter the element : "))
    l.append(element)

print(f"The original list is : {l}")

r = oddocurring(l)
print(f"The oddocuring number is {r}.")