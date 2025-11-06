s1 = {1,2,3,3,2,1,4,5,5}
print(s1)

s1 = {1 , 3, 5 ,7 ,9 , 10 ,67}
s2 = {1 , 2, 3, 4 ,5 , 56, 67}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))