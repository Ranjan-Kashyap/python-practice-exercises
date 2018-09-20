# Program to print a list of numbers from an existing list which are less than a given number

a = [1,1,2,4,5,77,44,2,4,232,232,565,774,24,1,23,965,432,263,8786786,4564,34534,2343,565]
x = []
number = int(input("Enter a number: "))

for element in a:
    if element < number:
        x.append(element)

print('Your new list is: ' + str(x))
