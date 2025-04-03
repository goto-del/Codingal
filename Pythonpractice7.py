x = 20
if(type(x) is int):
    print("Yes")
else:
    print("No")


x = 5.3
if(type(x) is not float):
    print("Yes")
else:
    print("No")

badge = 3
print("Bagde is",badge)


x = 20
y = 20
if ( x is y):
    print("x and y have same IDENTITY")

y = 10
x = 895
if ( x is not y ):
    print("x and y have DIFFERENT IDENTITY")


a = 10
b = -10

print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

a = 5
b = -10

print("a << 1 =", a << 1)
print("a << 1 =", b << 1)