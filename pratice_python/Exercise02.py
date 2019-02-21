"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.

2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


def get_number():
    return raw_input("Write number: ")


def is_number_even(aux_number):
    if int(aux_number) % 2 == 0:
        print "This number is even"
    else:
        print "This number is not even, it is odd"


def is_number_multiple_of_4(aux_multiple):
    if (aux_multiple & 3) == 0:
        return "{} is a multiple of 4"
    return "{} is not a multiple of 4"


def is_number_divided_another(aux_number, aux_number2):
    if int(aux_number) % int(aux_number2) == 0:
        print "{} divides {}".format(aux_number, aux_number2)
    else:
        print "{} does not divides {}".format(aux_number, aux_number2)


if __name__ == '__main__':
    number = get_number()
    is_number_even(int(number))
    print "extra"
    is_number_multiple_of_4(int(number))
    number2 = get_number()
    number3 = get_number()
    is_number_divided_another(number2, number3)
