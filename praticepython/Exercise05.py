"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (do not worry if you can not figure this out at this point - we will get to it soon)
"""


def match_element_from(list_a_aux, list_b_aux):
    print list(set(list_b_aux).intersection(set(list_a_aux)))


def randomly_generate_list():
    import random
    list_a = []
    list_b = []

    for element in range(11):
        list_a.append(random.randint(1, 101))

    for element in range(13):
        list_b.append(random.randint(1, 101))

    match_element_from(list_a, list_b)


if __name__ == '__main__':
    list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    match_element_from(list_a, list_b)

    randomly_generate_list()
