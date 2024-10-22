#35/36
#name = input("what's your name: ")
#num = int(input("pick a number: "))
#for x in range(num): #iterates for the amount of times they put in num
#    print(name) #outputs what they input in name

#37/38
#name = input("enter name: ")
#num = int(input("pick a number: "))
#for x in name:
#    for i in range(num):
#        print(x)

#39
#num = int(input("enter number between 1 and 12: "))
#for x in range(1,13): #iterate 12 times from 1 to 12
#    print(num, 'x', x, '=', num * x)

#40
#num = int(input("enter a number below 50: "))
#for x in reversed(range(1, 52)):
#    if x == num:
#        break #when x reaches the number inputted it will break at that number
#    else:
#        print(x - 1)

#41
#name = input("enter your name: ")
#num = int(input("enter a number: "))
#for x in range(num): #iterates for the amount of times inputted in num
#    if num < 10:
#        print(name)
#    else:
#        for x in range(1, 4): #nested for loop, prints "Too high" 3 times
#            print("Too high")
#        break #stops loop

#42
#total = 0
#for x in range(1, 6):
#    num = int(input("enter a number: "))
#    num_inc = input("do you want that number included y/n: ").lower()
#    if num_inc == "y":
#        total = total + num
#print(f"the total is {total}")

#43
#direction = input("which way do you want to count up or down: ").lower()
#if direction == "up":
#    top_num = int(input("enter the top number: "))
#    num = 1
#    for x in range(top_num):
#        print(num)
#        num = num + 1
#elif direction == "down":
#    num = int(input("enter a number below 20: "))
#    for x in reversed(range(1, 21)):
#        print(x)
#        x = x - 1
#        if x == num:
#            print(num)
#            break
#else:
#    print("I don't understand")

#44
people = int(input("how many people do you want to invite to my party: "))
if people < 10:
    for x in range(people):
        name = input("enter a name: ")
        print(f"{name} has been invited")
else:
    print("Too many people")