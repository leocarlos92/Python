"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
described below.

Discussion
Concepts for this week:

1. Functions
2. Reusable functions
3. Default arguments
"""


def get_number():
    return raw_input("Write a number: ")


def get_divisors_from2(number):
    return [num for num in reversed(range(2,number+1)) if number % num == 0 and number > 0]


def is_prime(num_aux):
    if len(get_divisors_from2(num_aux)) == 1:
        print '{} is a prime number'.format(num_aux)
    else:
        print '{} is not a prime number'.format(num_aux)


if __name__ == '__main__':
    num = get_number()
    is_prime(int(num))
