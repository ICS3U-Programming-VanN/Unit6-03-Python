#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: December 15, 2022
# This program generates 10 random numbers from
# 0-100 and then finds and displays the lowest/min
# number of all of them


import random

import constants


# This function finds and returns the min value of an array
def find_min_value(random_integers_list):
    # Initialized Variable to 101 (impossible to generate)
    lowest_number = 101

    # Goes through each index of the list to determine the lowest number
    for index in random_integers_list:
        # Checks if the index of the list is lower than the placeholder value for the lowest number
        if index < lowest_number:
            # Assigns the placeholder variable to the number in the index of the list
            lowest_number = index

    # Returns the min number to function call
    return lowest_number


def main():
    # Initialized List
    list_of_integers = []

    # Loops through 10 times to generate ten random numbers
    for counter in range(constants.MAX_LIST_SIZE):
        # Generates a random number from (0-100) and added it to a list
        list_of_integers.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))

        # Displays to console what number was added to the list and what position it is at
        print(f"{list_of_integers[counter]} added to the list at position {counter}")

    # Calls function to find the lowest number in the list
    min_number = find_min_value(list_of_integers)

    # Displays the min number to the console
    print(f"The min value: {min_number}")


if __name__ == "__main__":
    main()
