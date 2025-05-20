L = [2,7,1,15,9,7,12,9]
print("Original List: ", L)


count = 0

for i in L:
    count += i


avg = count / len(L)

print("sum = ", count)
print("Average = ", avg)


L.sort()

print("Smallest element is:", L[0])

print("Lrgest element is:", L[-1])