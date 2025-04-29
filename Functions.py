def well_wishes():
    print("Hello !")
    print("How are you?") 


well_wishes() 


def weather_condition():
    print("The weather is pleasant in ",spring)
    print("The weather is same in ",autumn)

spring = "autumn"
autumn = spring

weather_condition()


def add(P,Q):
    # This function is for adding two numbers
    return P + Q
def subract(P,Q):
    # This function is for subracting two numbers
    return P - Q
def multiply(P,Q):
    # This function is for multiplying two numbers
    return P * Q
def divide(P,Q):
    # This function is for dividing two numbers
    return P / Q

while True:
    print("Please select the operation") 
    print("a. Add")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")
    print("e. Exit")
    
    choice = (input("Please enter choice (a / b / c / d / e): "))
    


    num_1 = (int(input("Please enter the first number: ")))
    num_2 = (int(input("Please enter the second number: ")))

    if choice == "a":
        print (num_1, " + ", num_2, " = ", add(num_1, num_2))
    elif choice == "b":
        print (num_1, " - ", num_2, " = ", subract(num_1, num_2))
    elif choice == "c":
        print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))
    elif choice == "d":
        print (num_1, " / ", num_2, " = ", divide(num_1, num_2))
    elif choice == "e":
        break
    else:
        print("This is a invalid input")