"""
This Code is to ask the user to enter 5 different numbers on different lines,
Get the users response and ask them if they want to include it in the total,
And then calculate the sum excluding the ones the user doesn't want to include
"""


def get_users_response(question: str) -> bool:
    """To ask the user for confirmation"""
    """Break Statements are added to avoid infinite else warnings"""
    response = input(question + "[y/n] ")
    while True:
        if response == 'y':
            return True
        elif response == 'n':
            return False
        print("Please enter y(yes) or n(no)!")
        break


def user_questions(questions: list[str]):
    """To get users response and add them (The ones included)"""
    total = 0

    """The try except is to catch the value error made while answering the questions"""
    """The while True loop is to repeat the mistaken question again to make user-experience easy"""

    for question in questions:
        while True:
            try:
                num = int(input(question + ": "))
                break
            except ValueError:
                print("Please enter a valid input.")

        include = get_users_response(f"Include {num} in the total?")
        if include:
            num += 1

    print(f"The total number is {total}")


number_questions = ["Enter number 1",
                    "Enter number 2",
                    "Enter number 3",
                    "Enter number 4",
                    "Enter number 5"]


user_questions(number_questions)
















