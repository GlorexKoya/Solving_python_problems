"""
This a multiplication table based on user-input
"""

user_input = int(input("Enter the size of your Multiplication Table" 
"\n>>> "))     

for i in range(1, user_input + 1):
    for j in range(1, user_input + 1):
        print(f"{i * j : 4}", end="")
    print()    
