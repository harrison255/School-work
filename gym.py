import random

initial = input("What is your first initial: ")
surname = input("What is your surname: ")
membership = input("Would you like to sign up for the gym membership: ").lower()
if membership == "yes":
    paid = input("Please pay £30 type 'Paid' when you have: ")
    if paid == "Paid":
        print(f"Ok your membership name is {initial}{surname}.",random.randint(0,999))
else:
    print("Ok goodbye")