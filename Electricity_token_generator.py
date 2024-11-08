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

def transaction_id():
    """To get a dummy transaction ID for the receipt"""
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k','m','n','p','y','z']
    letters = rd.choice(letter)
    dummy_numbers = rd.randint(1, 99999)

    dummy_letters = rd.choice(letters) * 5
    print(f"2024{dummy_numbers}{dummy_letters}")


def transaction_date():
    """To make the transaction date look in this format"""
    # i.e Monday, Nov 2024
    date = dt.datetime.now()
    print(f"{date.strftime('%A')}, {date.strftime("%B")} {date.strftime("%Y")}")
    

def transaction_time():
    """To make the transaction time in this format"""
    #i.e. 01:20 PM
    time = dt.datetime.now()
    print(f"{time.strftime('%H')}:{time.strftime("%m")}{time.strftime("%p")}")


def customer_address():
    """To print a customer a dummy customers address using the random module"""
    #i.e. 20, Name Street off example road State, Nigeria.
    street_no = rd.randrange(1, 100)
    names_of_street = ['Ahmed', 'Bola', 'Saint Crus', 'Mudahshiru', 'Bamidele',
                       'Palmgroove', 'Olamire', 'Rihad', 'Pangolo', 'Juraimoh']
    names_of_road = ['Egbe', 'Iyana-Ipaja', 'Ojuelegba', 'Council', 'Ikotun', 'Liasu', 'Ile-iwe']
    names_of_state = ['Lagos', 'Ogun', 'Osun', 'Oyo', 'Ekiti']

    print(f"{rd.randrange(street_no)}, {rd.choice(names_of_street)} Street Off {rd.choice(names_of_road)} "
          f"{rd.choice(names_of_state)}, Nigeria.")


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
      f"\nCustomer Address : {customer_address()}"
      f"\nMeter Number: {meter_number}",
      f"\nMeter Type : {meter_type}",
      f"\nAmount : {amount}",
      f"\nTransaction Date : {transaction_date()}"
      f"\nTransaction Time : {transaction_time()}"),
