"""
A fun rock-paper-scissors game using the random module
"""

import random as rd

game = f"{'*' * 15} This is a (Rock/Paper/Scissors) game {'*' * 15}\n"
print(game)

users_name = input("Enter your name: ").capitalize()
print(f"Hey {users_name}, Welcome to Glorex (Rock/Paper/Scissors) game :)\n"
      f" You have to input between rock, paper or scissors \n"
      f" \n ..You can begin now..\n")

initial_trial = 0
max_trial = 5

print("..You have five trials..")
while initial_trial < max_trial:
    
    options = ['rock', 'paper', 'scissors']
    computers_choice = rd.choice(options)
    
    users_guess = input(" Pick your guess: ").lower()
 
    if computers_choice == 'rock':
        if users_guess == 'paper':
            print(f'  my guess is {computers_choice}') 
            print(' You win!')
       
    if computers_choice == 'paper':
        if users_guess == 'scissors':
            print(f' my guess is {computers_choice}')
            print('  You win!')
            
    if computers_choice == 'scissors':
        if users_guess == 'rock':
            print(f'  my guess is {computers_choice}')
            print('  You win!')
      
    if computers_choice == users_guess:
            print(f'  my guess is {computers_choice} also')
            print("  It's a tie =)")
     
    if computers_choice == 'rock':
        if users_guess == 'scissors':
            print(f'  my guess is {computers_choice}')
            print('  Aw, computer wins. ' 
                  'Try again :)')
        
    if computers_choice == 'scissors':
        if users_guess == 'paper':
            print(f'  my guess is {computers_choice}')
            print('  Aw, computer wins. ' 
                  'Try again :)')
  
    if computers_choice == 'paper':
        if users_guess == 'rock':
            print(f'  my guess is {computers_choice}')
            print('  Aw, computer wins. ' 
                  'Try again :)') 
                  
    initial_trial += 1  
    print() 
    print(f"..You have {max_trial - initial_trial} more tries..") 
         

print('Game over!')    
