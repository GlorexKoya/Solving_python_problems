"""Code just for fun.
To also test out the while True loop
This loop gives us the advantage to repeat a code when it is broken
or an invalid character has been inputted."""

balance = 400
print(f"Game balance: ${balance:.2f}")

while True:
    try:
        num = float(input("Deposit: "))     # This break statement will avoid any damage in code after a wrong
        break                                # character has been inputted
    except ValueError:
        print("Enter your deposit in number.")


balance += num
print(f" Updated Balance: ${balance:,.2f}")
























