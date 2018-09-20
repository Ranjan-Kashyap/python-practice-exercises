# Program to guess a number from 1 to 9 and tell whether the number is too close, too far or exact.
# Give the user option to exit when he types "exit" and also show how many guesses he made at the end.

import random
import sys

a = random.randint(1, 9)
stop = False
count = 0
while stop == False:
    count += 1
    userGuess = input("Enter your Guess: ")
    if str(userGuess) in ['exit', 'Exit']:
        sys.exit()
    elif abs(a - int(userGuess)) >= 5:
        print('Your Guess is too far from the number')
    elif abs(a - int(userGuess)) != 0 and abs(a - int(userGuess)) < 5:
        print('Your Guess is close to the number')
    else:
        print('Your Guess is Right')
        print('It took you ' + str(count) + ' Guesses to get this correct!')
        stop = True
