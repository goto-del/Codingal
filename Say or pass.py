for x in range(1,1000):   
    if x % 10 == 0:
        print("Twist")

    elif x % 15 == 0:
        pass

    elif x %5 == 0:
        print("Fizz")

    elif x %3 == 0:
        print("Buzz")

    else:
        print(x)