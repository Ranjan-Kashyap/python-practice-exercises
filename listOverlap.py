#Program to find the common elements of two lists and add them into new list
a = [1,2,3,6,9,10,13,14,15,16,17,38,45,34,74,35,90]
b = [3,6,7,9,11,20,2,54,13,17,89,54,90]

x = []

for element in a:
    if element in b:
            x.append(element)

print(x)
