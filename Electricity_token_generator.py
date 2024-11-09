"""
This code is to generate fake electricity token values using the random module
"""

import random as rd
import datetime as dt

print("\n..Da Glorex Official E-Token Store....")

name = input("\n  Enter your full name: ").title()
print("      Number Should be 11 numbers i.e 450123.....")
meter_number = int(input("  Enter your meter number: "))
user_input = input("  Prepaid or Postpaid[A/B]? ")
def meter_type():
    if user_input == 'A' or 'a':           # first time using a yield keyword. p.s: Just to practice
        yield 'Prepaid'                   # when using a yield keyword, you must always loop the function's object
    elif user_input == 'B' or 'b':       # for it to run because it pauses after the first execution
        yield 'Postpaid'
    else:
        yield 'Enter A or B!'

new = meter_type()
def inner_func():
    for i in new:
        return i

amount = int(input("  Enter amount: "))

def transaction_id():
    """To get a dummy transaction ID for the receipt"""
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k','m','n','p','y','z']
    letters = rd.sample(letter, k=5)
    dummy_numbers = rd.randint(1, 99999)
    dummy_numbers2 = rd.randint(1, 333)


    def dummy_letters():
        return ''.join(letters)

    return f"2024{dummy_numbers}{dummy_letters()}{dummy_numbers2}"


def transaction_date():
    """To make the transaction date look in this format"""
    # i.e Monday, Nov 2024
    date = dt.datetime.now()
    return f"{date.strftime('%A')}, {date.strftime("%B")} {date.strftime("%Y")}"
    

def transaction_time():
    """To make the transaction time in this format"""
    #i.e. 01:20 PM
    time = dt.datetime.now()
    return f"{time.strftime('%H')}:{time.strftime("%M")}{time.strftime("%p")}"


def customer_address():
    """To print a customer a dummy customers address using the random module"""
    #i.e. 20, Name Street off example road State, Nigeria.
    street_no = rd.randrange(1, 100)
    names_of_street = ['Ahmed', 'Bola', 'Saint Crus', 'Mudahshiru', 'Bamidele',
                       'Palmgroove', 'Olamire', 'Rihad', 'Pangolo', 'Juraimoh']
    names_of_road = ['Egbe', 'Iyana-Ipaja', 'Ojuelegba', 'Council', 'Ikotun', 'Liasu', 'Ile-iwe']
    names_of_state = ['Lagos', 'Ogun', 'Osun', 'Oyo', 'Ekiti']

    return(f"{rd.randrange(street_no)}, {rd.choice(names_of_street)} Street Off {rd.choice(names_of_road)} road "
          f"{rd.choice(names_of_state)}, Nigeria.")


# 0000-0000-0000-0000-0000         #How the values will look like
# Iterated over the random figure generator to give me new values after each iteration

def main_token():
    token = ""
    for num in range(5):
        e_token = rd.randint(0, 9999)
        token += str(e_token) + ("-" if num < 4 else "")  #The if block is to remove the delimiter '-' at the end of the last letter
    return token


print(f"\n {'.' * 20} ELECTRICITY RECEIPT {'.' * 20}"
      f"\n                 TOKEN : {main_token()}\n"
      f"\n    Transaction ID   :          {transaction_id()}",
      f"\n    Customer Name    :          {name}",
      f"\n    Customer Address :          {customer_address()}"
      f"\n    Meter Number     :          {meter_number}",
      f"\n    Meter Type       :          {inner_func()}",
      f"\n    Amount           :          {amount :.2f} Naira",
      f"\n    Transaction Date :          {transaction_date()}"
      f"\n    Transaction Time :          {transaction_time()}"),

print(f"\n  Thank you for Patronizing us {name}.")