"""
Code to ask user to input between top and down
If user inputs up, user will be asked to enter a number. It would then from print 1 to that number
If user inputs, down, it would print from the 20 to that number
"""

direction = input("Pick a direction (up/down): ").lower()
if direction == 'up':
    top_num = int(input("   Input top number: "))
    for x in range(1, top_num+1):
        print(x, end=", ")
    print()

    """If the user selects down"""
elif direction == 'down':
    down_num = int(input("  Input number below 20: "))
    for y in range(20, down_num-1, -1):
        print(y, end=", ")

    """If user enters an invalid input"""
else:
    print("Enter (up) or (down)!")
