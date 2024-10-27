"""
Code to remove fullstops and comas at the end of a word
"""

user_input = input("Enter any word: ")
stops = ("." or ",")

if user_input.endswith(stops):
    print(f"{user_input}\b")
else:
    print(user_input)


# if user_input == word:
#     print(f"{word}\b")
# else:
#     print(user_input)
