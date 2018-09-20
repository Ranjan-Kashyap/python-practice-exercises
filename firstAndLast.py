# Program that takes a list of numbers and makes a new list of only the first and last elements of the given list.

def myFunc():
    getNumbers = [int(x) for x in input("Enter the numbers of a list separated by space: ").split()]
    newList = [getNumbers[0], getNumbers[-1]]
    print('First and Last numbers of the list are: ' + str(newList))

myFunc()
