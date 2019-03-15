"""
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of
happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can not be divided by any other number. And yes,
happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
The explanation is easier with an example, which I will describe below.)
"""


def match_elements_common_from_file():
    with open("/home/leonarbc/PycharmProjects/training/practicepython/primenumbers.txt", 'r+') as primenumbers:
        with open("/home/leonarbc/PycharmProjects/training/practicepython/happynumbers.txt", 'r+') as happynumbers:
            primenumbers_list = map(lambda s: s.strip(), primenumbers.readlines())
            happynumbers_list = map(lambda s: s.strip(), happynumbers.readlines())
            print list(set(primenumbers_list).intersection(happynumbers_list))


if __name__ == '__main__':
    match_elements_common_from_file()
