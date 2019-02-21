"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""


def rules(player_1_aux, player_2_aux):
    if player_1_aux == player_2_aux:
        print "it is a draw"
    elif (player_1_aux == "rock" or player_1_aux == "Rock") and (player_2_aux == "scissors" or player_2_aux == "Scissors"):
        print "player 1 win, player 2 lose"
    elif (player_1_aux == "scissors" or player_1_aux == "Scissors") and (player_2_aux == "rock" or player_2_aux == "Rock"):
        print "player 2 win, player 1 lose"


def get_player_answer():
    return raw_input("what is your choose (Rock-Paper-Scissors)? ")


def get_answer_for_repeat_or_quit():
    return raw_input("do you want to repeat or quit? ")


if __name__ == '__main__':
    answer = 1
    while answer == 1:
        player_1 = get_player_answer()
        player_2 = get_player_answer()
        rules(player_1, player_2)
        get_answer_for_repeat_or_quit()
