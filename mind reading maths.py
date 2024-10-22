from time import sleep

name = input("I am the great magician Mysrical Meredith. What is your name? ")
print(f"Welcome {name}, I am going to perform a mind trick on you")
numInput = int(input("Pick a number  between 1 and 10: "))
print("Multiply the number by 2,")
sleep(2)
print("Multiply the new number by 5,")
sleep(3)
print("Divide the current number by the original number,")
sleep(3)
print("Subtract 7 from the original number.")
sleep(2)
enter = input("Press Enter when you're done.")

numNew = numInput*2
numNew = numNew / numInput
numNew = numNew - 7

print("Let me guess, your number is")
sleep(1)
print("Let me guess, your number is.")
sleep(1)
print("Let me guess, your number is..")
sleep(1)
print("Let me guess, your number is...")
sleep(2)
print(f"{numNew}!")
question = input("Did I get it right? ")