import random
import shutil
import os
number = random.randint(1,9)
print(number)

chances=0

while chances <5:
    guess=int(input("enter a number"))

    if guess==number:
        print("You Won")
        break
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

 
    chances += 1

if not chances <5:
        print("You lose !!! The number is", number)