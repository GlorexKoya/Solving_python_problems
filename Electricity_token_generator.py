"""
This code is to generate fake electricity token values using the random module
"""

import random as rd

# 0000-0000-0000-0000-0000         #How the values will look like
E_token = rd.randint(0, 9999)
print(E_token)

for num in range(5):
    print(E_token)
