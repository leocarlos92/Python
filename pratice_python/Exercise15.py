"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

    My name is Michele

Then I would see the string:

    Michele is name My

shown back to me.
"""


def get_long_string():
    long_string = raw_input("Write a long string: ")
    return long_string


def reverse_long_string(string_aux):
    str_long = string_aux.split()
    print str_long
    str_long.reverse()
    print " ".join(str_long)


if __name__ == '__main__':
    reverse_long_string(get_long_string())
