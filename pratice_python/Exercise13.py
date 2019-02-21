"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of
numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in
the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13 ...)
"""


def get_fibonnaci(fibonnaci, elements):
    if elements > 1:
        if len(fibonnaci) == 1:
            fibonnaci.append(fibonnaci[-1])
        else:
            fibonnaci.append(fibonnaci[-1] + fibonnaci[-2])
        elements -= 1
        get_fibonnaci(fibonnaci, elements)
    return fibonnaci


def get_elements():
    return raw_input("How many elements from Fibonnaci do you want?: ")


if __name__ == '__main__':
    print get_fibonnaci([1], int(get_elements()))
