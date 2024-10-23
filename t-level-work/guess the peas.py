print("Pick either Peas, Broccoli, Carrot or Sweetcorn")
print("I will attempt to guess your vegetable")
answer = input("Is the vegetable green?  Y/N: ").lower()
if answer == "n":
    answer = input("Is the vegetable orange? Y/N: ").lower()
    if answer == "y":
        print("It must be a Carrot!")
    else:
        print("It must be Sweetcorn!")
else:
    answer = input("Does the vegetable look like a tree? Y/N: ").lower()#line 14
    if answer == "y":
        print("It must be Brocolli!")
    else:
        print("It must be Peas!")
