def printes(n):   
    if(n<=0):
        return
    print("Codingal")
    print(n/2)
    printes(n/2)

printes(10)