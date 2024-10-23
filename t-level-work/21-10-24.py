#resort = ["Margate", "Swansea", "Brighton", "St Ives", "Cromer"]
#townName = "St Ives"
#n = 0
#while n < len(resort):
#    print(resort[n])
#    if townName == resort[n]:
#        found = True
#        break
#    n += 1

#69
#country_name = ["England", "Scotland", "Wales", "China", "Northern Ireland"]
#print(country_name)
#user_country = input("Enter one of these 5 countries: ")
#n = 0
#while n < len(country_name):
#    if user_country == country_name[n]:
#        print(n)
#        break
#    n += 1

#70
country_name = ["England", "Scotland", "Wales", "China", "Northern Ireland"]
print(country_name)
user_n = int(input("Enter index position"))
n = 0
try:
    while n < len(country_name):
        enumerate(country_name)
        if user_n == country_name[n]:
            print(country_name[n])
            break
        n += 1
except:
    print("Invalid index")
