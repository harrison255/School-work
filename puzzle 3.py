def sum_even(input_nums: list[int]):
    return sum(input_num for input_num in input_nums if input_num % 2 == 0)

print(sum_even([9, 7, 5, 3, 1]))