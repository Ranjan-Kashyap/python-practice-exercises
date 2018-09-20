# Program to make a new list of even numbers from a given list.

a = [1,2,3,4,5,6,7,8,9,12,24,35,73,63,52,84]
b =[]

for element in a:
    if element%2 == 0:
        b.append(element)

print(b)
