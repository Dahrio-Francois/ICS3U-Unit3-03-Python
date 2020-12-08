#!/usr/bin/env python 3
#
# Created by: Dahrio Francois
# Created on: December 2020
# this code randomly programs a number for a guessing game

import random
some_variable = random.randint(1, 50)  # a number between 1 and 50


def main():
    # this function sets up a random number for use

    # input
    guessing_number = int(input("Guess your number between 1 and 50: "))
    print("")

    # process
    if guessing_number > some_variable:
        print("Too High!")
        print("correct number is:")
        print(some_variable)
    elif guessing_number < some_variable:
        print("Too Low!")
        print("correct number is:")
        print(some_variable)
    elif guessing_number == some_variable:
        print("Correct!")


if __name__ == "__main__":
    main()
