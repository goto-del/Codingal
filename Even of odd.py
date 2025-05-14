import random
playing = True
number = random.randint(1,100)
print("Welcome!")
print("You have to tell if the number is even or odd.")
print("I have selected a number between 10 and 20.")
print(number)
while playing:
    what_he_said = input("Enter if its even of odd?: ")
    correct_answer = "even" if int(number) % 2 == 0 else "odd"

    if what_he_said == correct_answer:
        print("Congratulations!, you are correct!")
        break
    elif what_he_said == "exit":
        print("Bye")
        break
    elif what_he_said in ["even", "odd"]:
        print("Sorry, that's not correct. Try again! \n")
        break
    else:
        print("Please enter a valid answer")