my_set = {1,2,3}
print(my_set)

my_set = {1.0, "Hello", (1,2,3)}
print(my_set)

my_set = {1,2,3,4,3,2,1}
print(my_set)

my_set = set([1,2,3,2])
print(my_set,"\n")

my_set = {1,5,3,7,2,10,9,5,7}
my_set.pop()
print(my_set)

color_1 = {"red", "green", "blue"}
color_2 = {"yellow", "green", "blue"}
color_3 = color_1.union(color_2)
print("After union:", color_3)
color_4 = color_1.intersection(color_2)
print("After intersection:", color_4)
color_5 = color_1.difference(color_2)
print("After difference:", color_5)
color_6 = color_1.symmetric_difference(color_2)
print("After symmetric difference:", color_6)