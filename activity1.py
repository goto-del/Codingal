print("What is the type of the given database - \n 1) Relational Database \n 2) Non-Relational Database")
answer = int(input("Enter your guess here...."))
if answer == 2:
    print("You guessed it right!")

elif answer == 1:
    print("Ooops... You got it wrong!")

else:
    print("Please enter 1 or 2 / Please enter a valid number.")