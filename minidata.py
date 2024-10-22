initial = input("What is your first initial: ")
surname = input("What is your surname: ")
print("What is your age: ")
try:
    age = int(input())
except ValueError:
    print("That's not your age")
    age = int(input())
likes_marmite = input("True or false - you like marmite: ").capitalize()
marmite = "True"
decades = float(age/10)
print(f"Well hello {initial} {surname}")
print(f"It is {likes_marmite==marmite} that you like marmite")
print(f"This is probably because you are {decades} decades old")