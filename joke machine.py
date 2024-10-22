from time import sleep

score = 0
print("Welcome to Guess the Joke!")
sleep(2)
print("I will tell you the start of a joke,")
sleep(2)
print("Then you have to guess the answer.")
sleep(2)
print("If you guess correctly, you get a point!")
sleep(3)
print("Here comes the first joke!")
sleep(2)
joke = input("If the mushroom was such a fun guy why didn't they have the party at his house? ").lower() #REMEMBER BRACKETS AFTER .LOWER()
if joke == "there wasn't much-room" or joke == "there wasnt much-room" or joke == "there wasn't much room" or joke == "there wasnt much room":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("There wasn't much-room!")
print(f"Your score is: {score}")
sleep(3)
print("Here comes the next joke!")
sleep(2)
joke = input("Did you hear about the guy whose whole left side was cut off? ").lower() #REMEMBER BRACKETS AFTER .LOWER()
if joke == "he's all right now" or joke == "he's all right now" or joke == "he's alright now" or joke == "he's alright now":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("He's all right now.")
print(f"Your score is: {score}")
sleep(3)
print("Here comes the next joke!")
sleep(2)
joke = input("What biscuit does a short person like? ").lower() #REMEMBER BRACKETS AFTER .LOWER()
if joke == "shortbread":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")
    print("Shortbread.")
print(f"Your final score is: {score}")