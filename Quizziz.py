import random
print('Welcome to the Fruit color Quiz!')
print('You will be asked to identify the color of different fruits.')
print("Guess it to win 1 Million $")
class FruitQuiz:

    def __init__(self):

        self.fruit = {
            "Apple": "red",
            "Banana": "yellow",
            "Grapes": "green",
            "Orange": "orange",
            "Blueberry": "blue",
            "Strawberry": "red",
            "Lemon": "yellow",
            "Watermelon": "green",
            "Pineapple": "yellowish",
        }

    def quiz(self):
        while (True):

            fruit, color = random.choice(list(self.fruit.items()))

            print(f"What color is {fruit}?")
            user_answer = input()

            if(user_answer.lower() == color):
                print("Correect! You win 1 Million $")
            else:
                print(f"Wrong! The correct answer is {color}.")

            option = input("Do you want to play again? otherwise enter 1: ")
            if option == "1":
                break
        print("Thanks for playing! Goodbye!")
# Object creation
quiz = FruitQuiz()
quiz.quiz()
   