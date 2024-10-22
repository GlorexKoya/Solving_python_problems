"""
Code to ask for users name and a random number of their choice below 10
if they pick a number below 10, it would print their name that amount of times
Else anything number higher than 10 it would print "Too high three times"
"""

name_input = input("Enter your name: ")
num_input = int(input("Enter a number: "))

if num_input < 10:
    for i in range(num_input):
        print(name_input)
else:
    for x in range(3):
        print("Too high!")


# Testing
# name = 'glory'
# num= 9
# for i in range(num):
#     print(name)

