def get_users_response(question: str) -> bool:
    while True:
        response = input(question + "(y/n) ").lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Enter y(yes) or n(no)!")


def user_questions(questions: list[str]) -> dict[str, int]:

    responses = {}
    total = 0
    for question in questions:
        num = int(input(question))

        responses[question] = num
        # To input them in the dictionary i.e. responses[question] = key and num = value

        var = get_users_response("Do you want this number included in the total?")

        # # total = total + x
        #
        # if var == 'y':
        #     total += x
        # elif var == 'n':
        #     total -= x
        # else:
        #     pa

        if var:
            total += num

    print(f"The total number is {total}")
    return responses


questions = ["Enter number 1: ", "Enter number 2: ", "Enter number 3: ", "Enter number 4: ", "Enter number 5: "]
user_questions(questions)



# total = 0
# if get_users_response(user_questions(x)) == 'yes':
#     x += 1













# num_1 = int(input("Enter number 1"))
# num_2 = int(input("Enter number 2"))
# num_3 = int(input("Enter number 3"))
# num_4 = int(input("Enter number 4"))
# num_5 = int(input("Enter number 5"))
