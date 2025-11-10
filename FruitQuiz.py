import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {
            "Apple":"Red",
            "Banana":"Yellow",
            "Orange":"Orange",
            "Watermelon":"Green"

        }
    
    def quiz(self):
        while True:
            fruit = random.choice(list(self.fruits.keys()))
            color = self.fruits[fruit]
                                         
            print("What is the color of", fruit)

            if input().upper() == color.upper():
                print("Correct answer")
            else:
                print("Wrong answer. The correct color is", color)
            print("Do you want to continue? (yes/no)")
            if input().lower() != 'yes':
                break

print("Welcome to the Fruit Color Quiz!")
fq=FruitQuiz()
fq.quiz()