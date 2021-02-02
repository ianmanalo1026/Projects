import random


class Game:
    """Player will guess the random Number"""
    
    def __init__(self):
        self.name = None
        self.number = None
        self.random_number = None
        self.indicator = None
    
    def generateNumber(self):
        self.random_number = random.randint(1,5)
        return self.random_number
    
    def enterNumber(self):
        self.number = input("Enter Number:") 
        while type(self.number) is not int:
            try:
                self.number = int(self.number)
            except ValueError:
                self.number = input("Enter a valid Number:")
        return self.number
    
    def start(self):
        self.indicator = list()
        self.name = input("Your Name: ")
        self.random_number = self.generateNumber()
        print(f"Hi {self.name}")
        print("Start the game! You have 3 attempts to guess the number!")
        print("Guess the Number from 1 - 5")
        self.enterNumber()
        while len(self.indicator) <= 1:
            if self.number < self.random_number:
                self.indicator.append(self.number)
                print("higher")
                self.enterNumber()
            if self.number > self.random_number:
                self.indicator.append(self.number)
                print("lower")
                self.enterNumber()
            elif int(self.number) == int(self.random_number):
                print("You got it!")
                print(f"The random number is {self.random_number}")
                x = input("Would you like to play again? (yes or no): ")
                if x == "yes":
                    self.start()
                else:
                    print(f"Thanks for playing {self.name}")
                break
        print(f"The random number is {self.random_number}")
        x = input("Would you like to play again? (yes or no): ")
        if x == "yes":
            self.start()
        else:
            print(f"Thanks for playing {self.name}")


x = Game()
x.start()