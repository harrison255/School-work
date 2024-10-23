name = input("What is your name? ").lower() #.lower() converts any answer to lower case
if name == "anakin":
    print("How do you do Anakin!") #prints this message if name is anakin
elif name == "leia":
    print("The force is with you.") #prints this message if name is leia
else:
    print(f"Nice name, {name}") #prints this message if name is anything else
weather = input(f"So {name}, is it hot or cold where you are today? ").upper() #.upper() converts any answer to upper case
if weather == "COLD":
    print("You must be freezing!") #prints this message if weather is COLD
elif weather == "HOT":
    print("Drink plenty of water!") #prints this message if weather is HOT
else:
    print("I can't advise you on that type of weather.") #prints this message if weather is anything else
likes_blue = input("Do you like the colour blue? ").upper() #.upper() converts any answer to upper case
if likes_blue == "YES":
    print("I like blue too") #prints this message if blue is YES
else:
    print("That's a shame because I really like blue.") #prints this message if blue is anything else
#explorer task
country = input("What country are you from? ").lower()
if country == "england" or country == "britain": #make sure that after "or" you need to write the condition again
    print("God save the King")
elif country == "america" or country == "usa" or country == "us": #make sure that after "or" you need to write the condition again
    print("I love freedom")
else:
    print("That sounds like a good country, I want to go there some time")
travel = input("Can you take me to your country right now? ").lower()
while travel != "yes":
    print(f"Aw dangit pal, I've been meaning to go to {country} for a while now")
    travel = input("Please? ")
print("Awesome sauce my amigo, meet me at the airport")
print("My car just crashed nvm I can't come")
print("Have a good day! Bye!")
