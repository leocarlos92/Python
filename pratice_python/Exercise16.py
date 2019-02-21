"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a main method.

Extra:

1. Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""


def generator_password(characters):
    import string, random
    password = ""
    for char in range(characters):
        password = password + (random.choice(string.printable))
    return password


def get_answer():
    return raw_input("Do you want a new password: ")


if __name__ == '__main__':
    while True:
        print "Here is your new password: {} ".format(generator_password(10))
        answer = get_answer()
        if answer == 'no' or answer == 'NO':
            break
