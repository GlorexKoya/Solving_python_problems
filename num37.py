"""
Code to display the characters users name on new lines
Now we add a number input to print the characters on each line
that number of times based on the number input
"""

user_input = input("Enter your name: ")
user_input_num = int(input("Enter a number: "))

for x in range(user_input_num):
    for i in user_input:
        print(i)
    print()


