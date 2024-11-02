"""
A fun rock-paper-scissors game using the random module
"""

import random as rd

game = f"{'*' * 4}This is a (Rock/Paper/Scissors) game{'*' * 4}\n"
print(game)


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
            print(' you win!')
       
    if computers_choice == 'paper':
        if users_guess == 'scissors':
            print(f' my guess is {computers_choice}')
            print('  you win!')
            
    if computers_choice == 'scissors':
        if users_guess == 'rock':
            print(f'  my guess is {computers_choice}')
            print('  you win!')
      
    if computers_choice == users_guess:
            print(f'  my guess is {computers_choice} also')
            print("  it's a tie =)")
     
    if computers_choice == 'rock':
        if users_guess == 'scissors':
            print(f'  my guess is {computers_choice}')
            print('  aw, computer wins. ' 
                  'Try again :)')
        
    if computers_choice == 'scissors':
        if users_guess == 'paper':
            print(f'  my guess is {computers_choice}')
            print('  aw, computer wins. ' 
                  'Try again :)')
  
    if computers_choice == 'paper':
        if users_guess == 'rock':
            print(f'  my guess is {computers_choice}')
            print('  aw, computer wins. ' 
                  'Try again :)') 
                  
    initial_trial += 1  
    print() 
    print(f"..You have {max_trial - initial_trial} more tries..") 
         

print('Game over!')    
