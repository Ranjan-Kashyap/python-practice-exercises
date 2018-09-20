# Program to find out all the divisors of a number and put that in a list

number = int(input('Enter a number: '))
x = list(range(1, number+1))
y = []

for element in x:
    if number%element == 0:
        y.append(element)

print(y)
