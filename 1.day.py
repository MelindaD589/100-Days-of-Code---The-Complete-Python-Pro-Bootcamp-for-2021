# PROJECT: to create a band name generator

#1. Create a greeting for your program.
print("Hello! How are you today?")
#2. Ask the user for the city that they grew up in.
city = input("Where did you grow up?\n")
#3. Ask the user for the name of a pet.
pet = input("What was the name of your first pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)

# Hello! How are you today?
# Where did you grow up?
# Debrecen
# What was the name of your first pet?
# Swan
# Your band name could be Debrecen Swan

########################################################

# Practice
print("Hello world!\nHello world!")
#Hello world!
#Hello world!
# \n break the line, new line comes

print("Hello" + "Angela")
# HelloAngela

print("Hello" + "" + "Angela")
# Hello Angela

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print(''"Hello " + "world"'')')
print("New lines can be created with a backslash and n.")

# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

print("What is your name?")
# What is your name?

input("What is your name?")
# What is your name? _
print("Hello" + input("What is your name?") + "!")
# Hello Angela!

# Write a program that prints the number of characters in a user's name.
print(len(input("What is your name?")))

name = input("What is your name?")
# What is your name?Jack
print(name)
# Jack

name = input("What is your name?")
length = len(name)
print (length)

# Write a program that switches the values stored in the variables a and b.
# This is a common interview question
# example input a=3 b=5
a = input("a: ")
b = input("b: ")

# example output a=5 b=3
print("a: " + a)
print("b: " + b)

# answer
c = a
a = b
b = c