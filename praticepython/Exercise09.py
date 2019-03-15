"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

1. Keep the game going until the user types 'exit'
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""


def generate_number():
    import random
    return random.randint(1, 9)


def get_input():
    return raw_input("Write a number: ")


def guessing_number(num_generated, num, tries_aux):
    if int(num) == num_generated:
        print "number guessed {} is the same as generated randomly {}".format(num, num_generated)
        return

    if int(num) < num_generated:
        print "number guessed {} is lower as generated randomly {}".format(num, num_generated)
        guessing_number(num_generated, get_input())

    if int(num) > num_generated:
        print "number guessed {} is higher as generated randomly {}".format(num, num_generated)
        guessing_number(num_generated, get_input())


if __name__ == '__main__':
    while True:
        input = get_input()
        if input == 'exit':
            break
        else:
            guessing_number(generate_number(), input)
