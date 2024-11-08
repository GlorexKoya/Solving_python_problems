"""
This code is to generate fake electricity token values using the random module
"""

import random as rd
import datetime as dt

name = input("\nEnter your full name: ").title()
print("    Number Should be 11 numbers i.e 450123.....")
meter_number = int(input("Enter your meter number: "))
meter_type = input("Prepaid or Postpaid? ")
amount = int(input("Enter amount: "))

def transaction_date():
    """To make the transaction date look in this format"""
    # i.e Monday, Nov 2024
    date = dt.datetime.now()
    print(f"{date.strftime('%A')}, {date.strftime("%B")} {date.strftime("%Y")}")
    

def transaction_time():
    """To make the transaction time in this format"""
    #i.e 01:20 PM
    time = dt.datetime.now()
    print(f"{time.strftime('%H')}:{time.strftime("%m")}{time.strftime("%p")}")


# 0000-0000-0000-0000-0000         #How the values will look like
# Iterated over the random figure generator to give me new values after each iteration

def main_token():
    for num in range(5):
        e_token = rd.randint(0, 9999)
        if num == 4:                            #The if block is to remove the delimiter '-' at the end of the last letter
            print(e_token)
        else:
            print(e_token, end="-")


print(f"\n..................... ELECTRICITY RECEIPT..........................."
      f"        TOKEN : {main_token()}"
      f"\nTransaction ID : ",
      f"\nCustomer Name : {name}",
      f"\nCustomer Address : {}"
      f"\nMeter Number: {meter_number}",
      f"\nMeter Type : {meter_type}",
      f"\nAmount : {amount}",
      f"\nTransaction Date : {transaction_date()}"
      f"\nTransaction Time : {transaction_time()}"),
