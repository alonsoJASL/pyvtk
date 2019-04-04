#!/usr/bin/env python3
""" guesser.py, by JASL
This program has the user guess a number between
1 and 100
"""
import random

def main():
    print("Guess a number between 1 and 100.")
    randomNumber = random.randint(1,100)
    found = False

    while not found:
        userGuess = int(input("Your guess: "))
        if userGuess == randomNumber:
            print("You got it! ")
            found = True
        elif(userGuess > randomNumber):
            print("Guess lower!")
        else:
            print("Guess higher!")

    print("\nWell done")

if __name__ == "__main__":
    main()
