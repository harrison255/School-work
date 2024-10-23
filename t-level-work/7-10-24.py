#45
#total = 0
#while total <= 50:
#    num = int(input("enter a number: "))
#    total = total + num
#print(f"the total is {total}")

#46
#num = 0
#while num <= 5:
#    num = int(input("enter a number: "))
#print(f"the last number you entered was {num}")

#47
#yes = "y"
#total = 0
#while yes == "y":
#    num1 = int(input("enter a number: "))
#    num2 = int(input("enter another number: "))
#    total = total + num1 + num2
#    yes = input("type y if you want to enter more numbers: ").lower()
#print(f"the total is {total}")

#48
#count = 0
#yes = "y"
#while yes == "y":
#    name = input("enter a name: ")
#    print(f"{name} has been invited to the party")
#    count = count + 1
#    yes = input("do you want to invite another person: ")
#print(f"{count} people are coming to the party")

#49
#compnum = 50
#num = 0
#count = 0
#while num != compnum:
#    count = count + 1
#    num = int(input("guess the number: "))
#    if num > compnum:
#        print(f"too high")
#    elif num < compnum:
#        print(f"too low")
#print(f"well done, you took {count} attempts")

#50
#num = int(input("enter a number: "))
#while num <= 10 or num >= 20:
#    if num <= 10:
#        num = int(input("too low try again: "))
#    elif num >= 20:
#        num = int(input("too high try again: "))
#print("thank you")

#51
num = 10
while num != 0:
    print(f"there are {num} green bottles hanging on the wall,")
    print(f"{num} green bottles hanging on the wall,")
    print("if 1 green bottle should accidentally fall,")
    num = num - 1
    guess = int(input("how many green bottles will be hanging on the wall? "))
    while guess != num:
        guess = int(input("try again: "))
print("there are no more green bottles hanging on the wall")
