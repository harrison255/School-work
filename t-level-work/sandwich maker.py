total_cost = 0.00
SUGAR_TAX = 0.50
bread_type = input("Sandwich or Wrap? ").lower()
filling_type = input("Meat, Vegetarian or Vegan? ").lower()
sauce = input("Do you want sauce Y/N ").lower()
salad = input("what about a salad Y/N ").lower()
pudding = input("Cookie, Crisps, Fruit or none? ").lower()
drink = input("Fizzy drink, Water, Juice or none? ").lower()
if bread_type != "sandwich":
    total_cost = 2.00
else:
    total_cost = 3.00
if filling_type == "vegetarian" or filling_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50
if pudding == "cookie" and drink == "fizzy drink":
    total_cost = total_cost + SUGAR_TAX
if pudding == "none" and drink == "none":
    total_cost = total_cost - 0.50
if sauce == "y" and salad == "y":
    total_cost = total_cost + 1
print(f"Your total cost is:£{total_cost}")
