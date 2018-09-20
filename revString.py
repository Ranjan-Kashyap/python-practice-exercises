#Program that asks the user for a long string containing multiple words and
#prints back to the user the same string, except with the words in backwards order.

def revString():
    userInput = str(input("Enter your string: "))
    a = userInput.split()
    a.reverse()
    result = " ".join(a)
    print(result)

revString()
