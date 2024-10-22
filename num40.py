"""
Code to count from 50 to a user's input below 50 using loops
"""

user_input = int(input("Enter a number below 50: "))

# Using a for loop
for i in range(50, user_input - 1, -1):
    print(i)

# Using a while loop
if user_input < 50:
    while user_input > 0:
        print(user_input)
        user_input -= 1
else:
    print("Enter a number below 50!")
