"""
Let is say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""


def partial_list_from():
    return [even for even in list if even % 2 == 0]


if __name__ == '__main__':
    list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print partial_list_from()
