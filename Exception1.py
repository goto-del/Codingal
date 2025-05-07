try:
    num1, num2 = eval(input("Enter two numbers separated by a comma (,): "))
    result = num1 / num2
    print("The result is ",result)

except ZeroDivisionError:
    print("!! Division by zero is error !!")

except SyntaxError:
    print("Coma is missing. Enter the number separated by a comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions So the result is",result)

finally:
    print("This will execute no matter what!")