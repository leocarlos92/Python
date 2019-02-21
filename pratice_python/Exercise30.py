"""
This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
Download this file and save it in the same directory as your Python code. This file is Peter Norvig's compilation of the
dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

Hint: use the Python random library for picking a ra
"""


def pick_random_word():
    import re
    import random
    with open("/home/leonarbc/PycharmProjects/training/practicepython/sowpods.txt", 'r+') as filenames:
        pattern = re.compile(r'[\t\s\b\n]*(?P<name>\w+)[\t\s\b\n]+')
        match = re.findall(pattern, filenames.read())
        print random.choice(match)

if __name__ == '__main__':
    pick_random_word()
