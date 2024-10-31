import random as rd

game = f"{'*' * 4}This is a (Rock/Paper/Scissors) game{'*' * 4}\n"
print(game)


variable = ['rock', 'paper', 'scissors']
computer = rd.choice(variable)

user_guess = input("pick your guess: ").lower()
if computer == 'rock':
    if user_guess == 'paper':
        print(f' my guess is {computer}') 
        print(' you win!')
   
if computer == 'paper':
    if user_guess == 'scissors':
        print(f' my guess is {computer}')
        print(' you win!')
            
if computer == 'scissors':
    if user_guess == 'rock':
        print(f' my guess is {computer}')
        print(' you win!')
  
if computer == user_guess:
        print(f' my guess is {computer} also')
        print(" it's a tie =)")
     
if computer == 'rock':
    if user_guess == 'scissors':
        print(f' my guess is {computer}')
        print(' aw, computer wins. ' 
              'Try again :)')
        
if computer == 'scissors':
    if user_guess == 'paper':
        print(f' my guess is {computer}')
        print(' aw, computer wins. ' 
              'Try again :)')
  
if computer == 'paper':
    if user_guess == 'rock':
        print(f' my guess is {computer}')
        print(' aw, computer wins. ' 
              'Try again :)')
              
