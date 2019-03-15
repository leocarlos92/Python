"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""


def get_name():
    return raw_input("Write a word: ")


def is_palindrome(string_a_aux):
    if string_a_aux == reverse_string(string_a_aux):
        return True
    return False


def reverse_string(string_a_aux):
    return ''.join(reversed(string_a_aux))


if __name__ == '__main__':
    if is_palindrome(get_name()):
        print 'it is'
    else:
        print 'it is not '
