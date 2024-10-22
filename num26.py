print("....Enter a word you want to convert to pig latin....")

# test_word = 'glory'
# print(test_word.replace('g', 'h'))
# print(test_word.replace('g', ''))
# print(test_word.replace(test_word[0], ''))

user_input = input("Enter word: ")

a = user_input.replace(user_input[0], '')  # to replace the first letter with nothing
print(f"{a}ay")                                  # adding ay to the end of the word




