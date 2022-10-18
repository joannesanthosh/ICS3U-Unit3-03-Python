#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program gets the user to guess a number correctly or incorrectly

import random


def main():
    # this function checks if the guess is correct
    random_number = random.randint(0, 9)  # a number between 0 and 9

    # input
    user_guess = int(input("Enter a number between 0-9: "))
    print("")

    # process & output
    if user_guess == random_number:
        print("Correct guess!")
    else:
        print("Incorrect. The number was: {0}.".format(random_number))

        print("\nDone.")


if __name__ == "__main__":
    main()
