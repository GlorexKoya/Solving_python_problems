def get_users_response(question: str) -> bool:
    response = input("Do you want this number included?(y/n) ").lower()
    if response == 'y':
        return True
    elif response == 'n':
        return False
    else:
        print("Enter y(yes) or n(no)!")


def user_questions(questions: [str]) -> dict[str:int]:
    questions = ["Enter number 1: ",
                 "Enter number 2: ",
                 "Enter number 3: ",
                 "Enter number 4: ",
                 "Enter number 5: "]

    responses = {}
    total = 0
    for question in questions:
        x = int(input(question))
        responses[question] = x
        var = get_users_response("hii")

        if var == 'y':
            total += x
        elif var == 'n':
            continue
        else:
            pass

    print(f"The total number is {total}")


hii = print("Questions")
hey = user_questions([hii])

# total = 0
# if get_users_response(user_questions(x)) == 'yes':
#     x += 1













# num_1 = int(input("Enter number 1"))
# num_2 = int(input("Enter number 2"))
# num_3 = int(input("Enter number 3"))
# num_4 = int(input("Enter number 4"))
# num_5 = int(input("Enter number 5"))
