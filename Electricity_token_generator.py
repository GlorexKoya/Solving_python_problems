"""
This code is to generate fake electricity token values using the random module
"""

import random as rd

# 0000-0000-0000-0000-0000         #How the values will look like
# Iterated over the random figure generator to give me new values after each iteration


for num in range(5):
    E_token = rd.randint(0, 9999)
    if num == 4:                            #The if block is to remove the delimiter '-' at the end of the last letter
        print(E_token)
    else:
        print(E_token, end="-")
