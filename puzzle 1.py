letter = input("give a letter: ")
def filter_strings_containing_a(input_strs: list[str]):
    result = []
    for input_str in input_strs:
        if letter in input_str:
            result.append(input_str)

    return result

print(filter_strings_containing_a(["apple", "banana", "cherry", "date"]))