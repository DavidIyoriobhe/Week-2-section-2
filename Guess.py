#This is a guessing game
"""You are expected to enter numbers at random.
Please, follow the instructions given."""
import random
n = random.randint(1,10)
guess = int(input("Enter a number of your choice from 1 to 10: "))
while n!=guess:
    print
    if guess<n:
        print("You are close, please try again!")
        guess = int(input("Enter a number of your choice from 1 to 10: "))
    elif guess>n:
        print("You are not close, please try again!")
        guess = int(input("Enter a number of your choice from 1 to 10: "))
    else:
        print
        break
    print("You are correct!")
