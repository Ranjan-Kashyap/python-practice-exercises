#Program to generate strong passwords.

import string
import random

numbersTwo = list(range(100))
numbersOne = list(range(10))
specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '?', '/']
alphabetsLower = list(string.ascii_lowercase)
alphabetsUpper = list(string.ascii_uppercase)
pick1 = random.choice(numbersTwo)
pick2 = random.choice(alphabetsLower)
pick3 = random.choice(alphabetsUpper)
pick4 = random.choice(specialChars)
pick5 = random.choice(numbersOne)
pick6 = random.choice(alphabetsLower)
pick7 = random.choice(alphabetsUpper)
pick8 = random.choice(specialChars)
pick9 = random.choice(numbersTwo)
pick10 = random.choice(alphabetsLower)
pick11 = random.choice(alphabetsUpper)
pick12 = random.choice(specialChars)

result = [pick1, pick2, pick3, pick4, pick5, pick6, pick7, pick8, pick9, pick10, pick11, pick12]
random.shuffle(result)
password = ''.join(map(str, result))
print('Your new password is: ' + password)
