"""
A fun code to make sure user inputs 'a' which insists that user loves Glory.
If user enters a (They love Glory) the statement will iterate over and over until manually stopped.
If user enters other options, it would print a fun message and then start again.
"""


print("Do you love Glory?")
print(" a. Yes, I do\n",
      "b. No, I don't\n",
      "c. Maybe, not sure\n",
      "d. Not in the mood\n")


while True:
    try:
        answer = input("Pick an option: ")
        if answer == 'a':
            while answer == 'a':
                print(" You love Glory, ofc, who doesn't")
            break
        elif answer == 'b':
            print(" it's not possible, try again my love\n")
        elif answer == 'c':
            print(" You have to be sure, try again love\n")
        elif answer == 'd':
            print(" Dey play. Pick an option my love(muah)\n")
        else:
            print(" Enter one of the given options.\n")
    except ValueError:
        print(" Enter one of the given options.\n")


# while True:
#     if question == "Yes" or 'yes' or 'YES':
#         while question:
#             print("You love Glory")
#
