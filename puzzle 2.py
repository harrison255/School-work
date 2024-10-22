def sum_if_less_than_fifty(num_one: int, num_two: int):
    sum = num_one + num_two
    if sum >= 50:
        return None
    else:
        return sum
num_one = int(input("give a number: "))
num_two = int(input("give another number: "))
print(sum_if_less_than_fifty(num_one, num_two))