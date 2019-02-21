"""
This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.

Let's continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess,
letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual game,
the player can only guess 6 letters incorrectly before losing).

Let's say the word the player has to guess is "EVAPORATE". For this exercise, write the logic that asks a player
to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess
an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and
display a different message if the player tries to guess that letter again. Remember to stop the game when all
the letters have been guessed correctly! Don't worry about choosing a word randomly or keeping track of the number of
guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.
"""


def get_word_into_file():
    import re, random
    with open("/home/leonarbc/PycharmProjects/training/practicepython/sowpods.txt", 'r+') as filenames:
        pattern = re.compile(r'[\t\s\b\n]*(?P<name>\w+)[\t\s\b\n]+')
        match = re.findall(pattern, filenames.read())
        return random.choice(match)


def rule_game(word_aux):
    print word_aux
    tries = len(word_aux)*2
    while tries != 0:
        letter_guess = raw_input("Guess a letter: ")
        list_guess = []

        if letter_guess in list_guess:
            print "This letter was already a try"
            continue
        else:
            list_guess.append(letter_guess)

        for letter in list(word_aux):
            if word_aux[letter] == '*':
                continue
            if word_aux[letter] == letter_guess:
                word_aux[letter] = '*'
        tries -= 1


if __name__ == '__main__':
    word = get_word_into_file()
    rule_game(word)
