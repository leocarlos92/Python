"""
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
and another number.

The function decides whether or not the given number is inside the list and returns
(then prints) an appropriate boolean.

Extras:

1. Use binary search.
"""
import random


def randomly_generate_list():
    l = []
    for element in range(10):
        l.append(random.randint(1, 101))
    return list(set(l))


def is_number_inside_list():
    lista = randomly_generate_list()
    lista.sort()
    num = random.randint(1, 101)
    print lista
    print num
    if num in lista:
        print "found it"
    else:
        print "not found it"


if __name__ == '__main__':
    is_number_inside_list()
