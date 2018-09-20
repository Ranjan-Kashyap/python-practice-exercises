# Program to find out if a number is prime or not
# Prime numbers is a number that has no divisor

number = int(input('Enter a number: '))
x = list(range(1, number+1))
y = []
z = [1, number]

for element in x:
    if number%element == 0:
        y.append(element)

if y == z:
    print('It is a prime number')
else:
    print('It is not a prime number')
