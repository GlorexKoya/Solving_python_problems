print("....Enter a word you want to convert to pig latin....")
# test_word = 'glory'
# print(test_word.replace('g', 'h'))
# print(test_word.replace('g', ''))
# print(test_word.replace(test_word[0], ''))
#
# a = test_word[0]
# b = test_word.replace(a, '')
# print(f"{b}{a}ay")

user_input = input("Enter word: ")

a = user_input[0]                      # assigning the first index to a variable to be useable later
b = user_input.replace(a, '')    # to replace the first letter with nothing
print(f"{b}{a}ay")                      # adding ay to the end of the word
                                        # adding the first letter before the ay

