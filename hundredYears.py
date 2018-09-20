#Program to tell when you will turn 100 years old

name = input("Enter your name: ")
age = int(input("Enter your age: "))
currentYear = int(input("Enter current year: "))
year = currentYear + (100 - age)

print(name + ", you will turn 100 years old in the year: " + str(year))
