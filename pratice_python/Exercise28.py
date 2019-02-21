"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!
"""


def get_var():
    return raw_input("Insert a input: ")


def get_max(var1_aux, var2_aux, var3_aux):
    return max(var1_aux, var2_aux, var3_aux)


if __name__ == '__main__':
    var1 = get_var()
    var2 = get_var()
    var3 = get_var()
    print get_max(var1, var2, var3)
