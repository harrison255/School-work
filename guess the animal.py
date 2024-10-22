print("Pick either Ostrict, Lion, Fish or Whale")
print("I will attempt to guess your choice")
answer = input("Does the animal live in the water?  Y/N: ").lower()
if answer == "n":
    answer = input("Does the animal have wings? Y/N: ").lower()
    if answer == "y":
        print("It must be an Ostrich!")
    else:
        print("It must be a Lion!")
else:
    answer = input("Is the animal a mammal? Y/N: ").lower()#line 14
    if answer == "y":
        print("It must be a Whale!")
    else:
        print("It must be a Fish!")