"""
A fun rock-paper-scissors game using the random module
"""

import random as rd
from os import PathLike

game = f"{'*' * 15} This is a (Rock/Paper/Scissors) game {'*' * 15}\n"
print(game)

users_name = input("Enter your name: ").capitalize()
print(f"Hey {users_name}, Welcome to Glorex (Rock/Paper/Scissors) game :)\n"
      f" You have to input between rock, paper or scissors \n"
      f"  Input (r) for rock, (p) for paper, (s) for scissors\n"
      f"   You can begin now!\n")

initial_trial = 0
max_trial = 5
user_result_counter = 0
computer_result_counter = 0

print("***..You have 5 trials..***")
while initial_trial < max_trial:
    
    options = ['r', 'p', 's']
    computers_choice = rd.choice(options)
    
    users_guess = input(" Pick your guess: ").lower()
 
    if computers_choice == 'r':
        if users_guess == 'p':
            print(f'  my guess is rock')
            print("  You win!")
            user_result_counter += 1

    if computers_choice == 'p':
        if users_guess == 's':
            print(f' my guess is paper')
            print("  You win!")
            user_result_counter += 1

    if computers_choice == 's':
        if users_guess == 'r':
            print(f'  my guess is scissors')
            print("  You win!")
            user_result_counter += 1

    if computers_choice == users_guess:
        if users_guess == 'r':
            print(f'  my guess is rock also')
        elif users_guess == 'p':
            print(f'  my guess is paper also')
        elif users_guess == 's':
            print(f'  my guess is scissors also')
        print("  It's a tie =)")

    if computers_choice == 'r':
        if users_guess == 's':
            print(f'  my guess is rock')
            print('  Aw, computer wins this round :)')
            computer_result_counter += 1
        
    if computers_choice == 's':
        if users_guess == 'p':
            print(f'  my guess is scissors')
            print('  Aw, computer wins this round :)')
            computer_result_counter += 1

    if computers_choice == 'p':
        if users_guess == 'r':
            print(f'  my guess is paper')
            print('  Aw, computer wins this round :)')
            computer_result_counter += 1

    initial_trial += 1
    print()
    print(f"..You have {max_trial - initial_trial} more tries..")

print('Game over!')

"""Just to style the Final Game Results"""

print(f"\n {'.' * 30}FINAL RESULT{'.' * 30}")

if user_result_counter > computer_result_counter:
    print(f"{' ' * 23}{users_name}({user_result_counter}) - Computer({computer_result_counter})")
    print(f"   {' ' * 25}{users_name.upper()} WINS!"
          f"\n {' ' * 25}GOODJOB {users_name}")

elif user_result_counter < computer_result_counter:
    print(f"{' ' * 23}Computer({computer_result_counter}) - {users_name}({user_result_counter})")
    print(f"{' ' * 27}COMPUTER WINS!"
          f"\n {' ' * 20}You tried pal, No hard feelings.")

elif user_result_counter == computer_result_counter:
    print(f"{' ' * 25}{users_name}({user_result_counter}) - Computer({computer_result_counter})")
    print(f"{' ' * 24}It's a tie! Well done {users_name}")
