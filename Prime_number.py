"""
Code to check if a users number is a prime number
A prime number is a number that is cannot be divided by two and can be devided by itself
Note: 0 and 1 are not prime numbers.
"""

print()
print("..Check if number is a prime number..")
number = int(input("Enter a number: "))

while True:
    try:
        if number < 2:
            print(f"{number} is not a prime number")
            break
        elif number == 2:
            print(f"{number} is a prime number")
        elif number % 2 == 0:
            print(f"{number} is not a prime number")
        elif number / number == 1:
            print(f"{number} is a prime number")
        else:
            print("Enter a whole number")
    except ValueError:
        print("please enter a whole number.")

