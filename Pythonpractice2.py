a = 5
print("type of a:" , type(a))
print(a)

b = 2.5
print("type of b:" , type(b))
print(b)

c = "codingal"
print("type of c:" , type(c))
print(c)

d = True
print("type of d:" , type(d))
print(d)
#Number of badges Ma'am have to give.
badges = 0
print(badges)
name = "Elias"
Age = 9
is_student = True
Weight = 28.6
NewWeight = int(29.3)

print("Name :" , name)
print("Data type of Name is" , type(name))

print("Age :" , Age)
print("Data type of Age is" , type(Age))

print("is_student :" , is_student)
print("Data type of is_student is" , type(is_student))

print("Weight :" , Weight)
print("Data type of Weight is" , type(Weight))

print("My new weight is :" , NewWeight)
print("Data type of NewWeight is" , type(NewWeight))

text = str(input("Enter a string"))

RevText = text[: : -1]
text = RevText

print("Reverse of Given string is:")
print(text)