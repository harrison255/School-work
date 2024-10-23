#12
num1 = int(input("give a number: "))
num2 = int(input("give a number: "))
if num1 > num2:
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)
#13
num20 = int(input("give number under 20: "))
if num20 >= 20:
    print("too high")
else:
    print("thank you")
#14
num1020 = int(input("enter number between 10 and 20: "))
if num1020 >= 10 and num1020 <= 20:
    print("thank you")
else:
    print("INCORRECT ANSWER")
#15
colour = input("what's your favourite colour: ").lower()
if colour == "red":
    print("i like red too")
else:
    print(f"i don't like {colour}, i prefer red")
#16
rain = input("is it raining: ").lower()
if rain == "yes":
    wind = input("is it windy: ").lower()
    if wind == "yes":
        print("too windy for an umbrella")
    else:
        print("take an umbrella")
else:
    print("enjoy your day")
#17
age = int(input("what's your age: "))
if age >= 18:
    print("you can vote")
elif age == 17:
    print("you can learn to drive")
elif age == 16:
    print("you can buy a lottery ticket")
else:
    print("you can go Trick-or-Treating")
#18
numrange = int(input("enter number: "))
if numrange < 10:
    print("too low")
elif numrange >= 10 and numrange <= 20:
    print("correct")
else:
    print("too high")
#19
num123 = int(input("enter 1, 2 or 3: "))
if num123 == 1:
    print("thank you")
elif num123 == 2:
    print("well done")
elif num123 == 3:
    print("correct")
else:
    print("error message")
