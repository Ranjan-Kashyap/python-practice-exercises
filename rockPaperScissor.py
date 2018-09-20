# Program to play rock paper scissor game with the computer
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random
stop = False
while stop == False:
    playerHuman = str(input("Enter your input - \"Rock\", \"Paper\" or \"Scissor\": "))
    possibleActions = ['Rock', 'Paper', 'Scissor']
    playerComputer = str(random.choice(possibleActions))
    print('Your Choice: ' + playerHuman)
    print('Computer\'s choice: ' + playerComputer )
    if playerHuman in ['Rock', 'rock'] and playerComputer in ['Scissor', 'scissor'] or playerHuman in ['Scissor', 'scissor'] and playerComputer in ['Paper', 'paper'] or playerHuman in ['Paper', 'paper'] and playerComputer in ['Rock', 'rock']:
        print("Congratulations, you won the game")
        wantToPlayMore = str(input('Do you want to play more? Type \"Y\" for Yes and \"N\" for No: '))
        if wantToPlayMore in ['N', 'n']:
                    stop = True
    elif playerComputer in ['Rock', 'rock'] and playerHuman in ['Scissor', 'scissor'] or playerComputer in ['Scissor', 'scissor'] and playerHuman in ['Paper', 'paper'] or playerComputer in ['Paper', 'paper'] and playerHuman in ['Rock', 'rock']:
        print("You lost the game")
        wantToPlayMore = str(input('Do you want to play more? Type \"Y\" for Yes and \"N\" for No: '))
        if wantToPlayMore in ['N', 'n']:
                    stop = True
    else:
        print('                                                     ')
        print("__________________________It's a Tie, Play Again__________________________")
        print('                                                     ')
