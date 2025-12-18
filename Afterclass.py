def sum(n,m):
    
    return n * m


n = int(input("Enter a number : "))
m = int(input("Enter a number : "))

s = sum(n,m)
print(s)

def wow(n,m):

    result = 0
    for i in range(m):
        result = result+n

    return result

n1 = int(input("Enter a number : "))
m1 = int(input("Enter a number : "))

s1 = wow(n1,m1)
print(s1)