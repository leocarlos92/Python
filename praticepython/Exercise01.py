"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of
the previous message.
(Hint: order of operations exists in Python)

2. Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)

"""


def get_name():
    return raw_input("Write your name: ")


def get_age():
    return raw_input("Write your age: ")


def get_years_remaining_to_one_hundred(aux_age):
    import datetime
    return int(datetime.datetime.now().year) + (100 - int(aux_age))


if __name__ == '__main__':
    print "Write name and age to estimate what years would you get 100 years old"
    name = get_name()
    age = get_age()
    print "{} would get 100 years old in {}, since he is {}".format(name, get_years_remaining_to_one_hundred(age), age)
