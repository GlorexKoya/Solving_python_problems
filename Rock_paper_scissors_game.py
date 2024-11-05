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
      f"  You can begin now!\n")

initial_trial = 0
max_trial = 5
user_result_counter = 0
computer_result_counter = 0

print("***..You have 5 trials..***")
while initial_trial < max_trial:
    
    options = ['rock', 'paper', 'scissors']
    computers_choice = rd.choice(options)
    
    users_guess = input(" Pick your guess: ").lower()
 
    if computers_choice == 'rock':
        if users_guess == 'paper':
            print(f'  my guess is {computers_choice}')
            print("  You win!")
            user_result_counter += 1

    if computers_choice == 'paper':
        if users_guess == 'scissors':
            print(f' my guess is {computers_choice}')
            print("  You win!")
            user_result_counter += 1

    if computers_choice == 'scissors':
        if users_guess == 'rock':
            print(f'  my guess is {computers_choice}')
            print("  You win!")
            user_result_counter += 1
      
    if computers_choice == users_guess:
            print(f'  my guess is {computers_choice} also')
            print("  It's a tie =)")

    if computers_choice == 'rock':
        if users_guess == 'scissors':
            print(f'  my guess is {computers_choice}')
            print('  Aw, computer wins this round :)')
            computer_result_counter += 1
        
    if computers_choice == 'scissors':
        if users_guess == 'paper':
            print(f'  my guess is {computers_choice}')
            print('  Aw, computer wins this round :)')
            computer_result_counter += 1

    if computers_choice == 'paper':
        if users_guess == 'rock':
            print(f'  my guess is {computers_choice}')
            print('  Aw, computer wins this round :)')
            computer_result_counter += 1

    initial_trial += 1  
    print() 
    print(f"..You have {max_trial - initial_trial} more tries..") 

print('Game over!')
print()

if user_result_counter > computer_result_counter:
    print(f" {'*' * 10} The final score is {users_name}({user_result_counter}) - Computer({computer_result_counter}) {'*' * 10}")
    print(f"  {users_name} wins!")
elif user_result_counter < computer_result_counter:
    print(f" {'*' * 10} The final score is Computer({computer_result_counter}) - {users_name}({user_result_counter}) {'*' * 10}")
    print(f"  Computer wins!")
elif user_result_counter == computer_result_counter:
    print(f"  It's a tie! Well done {users_name}")
