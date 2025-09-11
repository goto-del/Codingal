import numpy as np

array1 = np.array([1, 3, 4, 6, 9, 2, 8, 5, 7, 10])
array2 = np.array([1, 3, 4, 6])
newarray = np.concatenate((array1, array2))
print(newarray) 

print(np.sort(newarray))