"""
Code to ask for users name and a random number of their choice below 10
if they pick a number below 10, it would print their name that amount of times
Else anything number higher than 10 it would print "Too high three times"
"""

user_name_input = input("Enter your name: ")
user_num_input = int(input("Enter a number: "))

if user_num_input < 10:
    for i in range(user_num_input):
        print(user_name_input)
else:
    for x in range(3):
        print("Too high!")


# Testing
# name = 'glory'
# num= 9
# for i in range(num):
#     print(name)

