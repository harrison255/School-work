import random
from random import randint
import time

credit = 1
machine = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
playing = "yes"
while playing == "yes":
    playing = input("Do you want to spin the machine? ").lower()
    if playing == "yes":
        print("Spinning...")
        time.sleep(3)
        spin_1 = (random.choice(machine))
        time.sleep(1)
        spin_2 = (random.choice(machine))
        time.sleep(2)
        spin_3 = (random.choice(machine))
        print(spin_1, spin_2, spin_3)
        if spin_1 == spin_2 or spin_2 == spin_3 or spin_1 == spin_3:
            credit = credit + 0.5
    print("You left with £", credit)
