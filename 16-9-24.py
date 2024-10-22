name = input("whats your name: ")
print(f"hello {name}")

name = input("whats your name: ")
surname = input("whats your last name: ")
print(f"hello {name} {surname}")

print("What do you call a bear with no teeth?\nA gummy bear!")

num1 = int(input("give a number: "))
num2 = int(input("give another number: "))
print("The total is", num1+num2)

num1 = int(input("give number: "))
num2 = int(input("give another number: "))
num3 = int(input("give third number: "))
print("The answer is", (num1+num2)*num3)

slice_start = int(input("how many slices of pizza were there: "))
slice_eat = int(input("how many slice you eat: "))
print("There are", slice_start-slice_eat, "slices left.")

name = input("whats your name: ")
age = int(input("how old are you: "))
print(f"{name} next birthday you will be", age+1)

total_bill = float(input("what's the total price of the bill: "))
diners = int(input("how many diners: "))
print("each person must pay", total_bill/diners)

days = int(input("enter number of days: "))
hours = 24 * days
minutes = 1440 * days
seconds = 86400 * days
print(f"hours: {hours}\nminutes: {minutes}\nseconds: {seconds}")

kg = float(input("enter weight in kg: "))
print("weight in pounds is", kg*2.205)

big_num = int(input("enter a number over 100: "))
small_num = int(input("enter a number under 10: "))
print(f"{small_num} goes into {big_num}", big_num//small_num, "times")