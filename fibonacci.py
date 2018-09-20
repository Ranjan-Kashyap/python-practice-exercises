# Program that asks the user how many Fibonnaci numbers to generate and then generates them.

a = int(input('How many Fibonacci numbers you want to generate: '))
b = a - 1
x = 0
z = 1
start = 0
if a == 0:
    y = []
else:
    y = [1]
    while start < b:
        result = x + z
        y.append(result)
        x = z
        z = result
        start += 1
print(y)
