import random
import math

def play():
    print('\n')
    user = input("Enter your choice, 'R' for Rock, 'P' for Paper, 'S' for Scissors \n")
    user = user.lower()
    while user != 'r' and user != 'p' and user != 's':
        print("Please enter a valid letter")
        user = input("Enter your choice, 'R' for Rock, 'P' for Paper, 'S' for Scissors \n").lower()
    print('\n')

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0,user,computer)

    if is_win(user,computer):
        return (1,user,computer)

    return (-1,user,computer)

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
      return True
    return False

def play_best_of(n):

    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)

    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()

        if result == 0:
            print(" You chose {}, and Computer chose {}. its a tie".format(user,computer))

        elif result == 1:
            player_wins += 1
            print("You chose {}, and Computer chose {}, You won!".format(user,computer))
        
        else:
            computer_wins += 1
            print("You chose {}, and Computer chose {}, You lost! ")
    if player_wins > computer_wins:
        print("You have won best of {} games".format(n))
    else:
        print("You lost, Copmuter has won the best of {} games".format(n))

# if _name_ == '_main_':
def start():
    print("Welcome, Let's Play a Game \n")
    play_best_of(3)

start()