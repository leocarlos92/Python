"""
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements less than 5
from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that
are smaller than that number given by the user.

"""


def get_list_with_elements_minus(aux_number):
    return [numbers for numbers in list if numbers < aux_number]


def get_number():
    return raw_input("Write a number: ")


if __name__ == '__main__':
    list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    print "{} numbers that are minus that 5 in this {} list".format(get_list_with_elements_minus(5), list)
    print "Extra: {} numbers that are minus that 5 in this {} list".format(get_list_with_elements_minus(int(get_number())), list)
