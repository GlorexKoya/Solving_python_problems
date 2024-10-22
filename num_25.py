# To get the length of users name
user_input = input("enter your name: ")
len_user_input = len(user_input)

# if the length of the users name is less than 5
# we would tell them to add their surname and print both of them together in uppercase
if len_user_input < 5:
    a = (input("Enter your Surname: "))
    b = f"{user_input}{a}".upper()
    print(b)
else:  # else, if it is higher than 5, we would print it in lowercase
    print(user_input.lower())

