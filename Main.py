import numpy as np

a = np.array([1, 3, 4, 6, 9, 2, 8, 5, 7, 10, 13, 15, 17, 21, 16, 19, 14, 11, 12, 18, 20])
print(a)

#This shows the type of 'a'
print(type(a))

#This prints the 4th element in the array
print(a[3])

#This prints elements from index 0 to 4 (5 is excluded)
print(a[0:5])

#This shows a.dype
print(a.dtype)

b = np.array([1, 3, 4, 6], dtype='float32')

print(b)

c = np.array([1, 2, 3], dtype='S')

print(c)

print(a.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
newarr = arr.reshape(10, 2)
print(newarr)