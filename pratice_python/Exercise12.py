"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
the first and last elements of the given list. For practice, write this code inside a function.
"""


def sublist_first_last(list_a_aux):
    return [list_a_aux[0],list_a_aux[-1]]


if __name__ == '__main__':
    list_a = [5, 10, 15, 20, 25]
    print sublist_first_last(list_a)
