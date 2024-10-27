"""
This code is to check if a users word is a palindrome. i.e. The same spelling as backwards
"""

print()
user_input = input("Enter a word: ")
back_word = user_input[::-1]

if back_word == user_input:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")
















