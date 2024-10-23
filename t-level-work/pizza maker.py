total_cost = 0.00
base_type = input("Thick or thin crust? ").lower()
size = input("Pick pizza size: 8, 10, 12, 14, 18 inch: ")
cheese = input("Do you want cheese Y/N: ")
pizza_type = input("What pizza do you want: Margarita, Vegetable, Vegan, Hawaiian, Meat feast: ")
voucher_code = input("Do you have a voucher Y/N: ")

if base_type == "thick":
    total_cost = total_cost + 8.00
else:
    total_cost = total_cost + 10.00
if size == "12" or size == "14" or size == "18":
    total_cost = total_cost + 2.00
if cheese == "n":
    total_cost = total_cost - 0.50
if pizza_type == "vegetable" or pizza_type == "vegan":
    total_cost = total_cost + 1.00
if pizza_type == "hawaiian" or pizza_type == "meat feast":
    total_cost = total_cost + 2.00
if voucher_code == "y":
    voucher_input = input("Enter voucher code: ")
    if voucher_input == "FunFriday":
        total_cost = total_cost - 2.00
        print("Redeemed successfully")

print(f"Your {base_type} crust {size} inch {pizza_type} pizza will cost £{total_cost}")
