from random import randint
num = randint(1,10)
print(num)
guess = int(input("guess a number between 1 and 10: "))
count = 1
while guess != num and count <= 3:
    print("incorrect")
    guess = int(input("guess a number between 1 and 10: "))
    count = count + 1
    print(count)
if count < 4:
    print("correct")
    print(f"you guessed it in {count} attempts")
else:
    print("incorrect, guess limit reached")
