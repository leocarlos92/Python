"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you do not know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""


def get_number():
    return raw_input("Write a number: ")


def get_divisors_from(number, cont_number):
        if cont_number == 0:
            return
        elif number % cont_number == 0:
            list_divisors.append(cont_number)
        cont_number = cont_number -1
        get_divisors_from(number, cont_number)


def get_divisors_from2(number):
    return [num for num in reversed(range(1,number+1)) if number % num == 0 and number > 0]


if __name__ == '__main__':
    list_divisors = []
    number_from_user = get_number()
    get_divisors_from(int(number_from_user), int(number_from_user))
    print "first way"
    print list_divisors
    print "second way"
    print get_divisors_from2(int(number_from_user))
