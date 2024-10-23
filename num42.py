def get_users_response(question: str) -> bool:
    response = input("Do you want this number included?(yes/no) ").lower()
    if response == 'yes':
        return True
    elif response == 'no':
        return False
    else:
        print("Enter yes or no!")


def user_questions(questions: list[str]) -> int:
    questions = ["Enter number 1: ",
                 "Enter number 2: ",
                 "Enter number 3: ",
                 "Enter number 4: ",
                 "Enter number 5: "]


total = 0
if get_users_response(user_questions(x)) == 'yes':
    x += 1













# num_1 = int(input("Enter number 1"))
# num_2 = int(input("Enter number 2"))
# num_3 = int(input("Enter number 3"))
# num_4 = int(input("Enter number 4"))
# num_5 = int(input("Enter number 5"))
