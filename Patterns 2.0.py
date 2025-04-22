print("Numbers half pyramid")
n = (int(input("Enter the rows: ")))
c = 1
for i  in range(n):
    for j in range(i + 1):
        print(c  , end=" ")
        c = c+1

    print()



rowSize = int(input("Enter the number of rows: "))
if rowSize%2==0: 
    halfDiamRow = int(rowSize / 2)+1
else:
    halfDiamRow = int(rowSize / 2)+1
    
space = halfDiamRow-1

for i in range(1, halfDiamRow+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        
        num = num+1

    print()