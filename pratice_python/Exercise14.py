"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
list minus all the duplicates.

Extras:

1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""


def get_list_without_duplicates(list_aux):
    print list(set(list_aux))


if __name__ == '__main__':
    list_a = [1, 1, 2, 3, 3, 4, 5, 6, 6]
    get_list_without_duplicates(list_a)
