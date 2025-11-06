s1 = {"Cow", "Dog", "Cat", "Elephant", "Tiger", "Dog"}
s2 = {"Lion", "Deer", "Cat", "Dog", "Monkey", "Tiger"}
print(s1)
print(s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))