def squaretime(n):
    iteration = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*", end = " ")
            iteration += 1

        print(" ")
    print("Total number of iterations done by the code is : ",iteration)    
    
squaretime(5)
squaretime(10)
squaretime(234)