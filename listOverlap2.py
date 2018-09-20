#Program to find the common elements of two lists and add them into new list. Also don't repeat any element
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

x = []

for element in a:
    if element in b and element not in x:
            x.append(element)

print(x)
