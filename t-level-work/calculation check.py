def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

def multiply(a, b):
    answer = a * b
    print(f"{a} x {b} = {answer}")

def subtract(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")

def divide(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")

again = "y"
while again == "y":
    num1 = int(input("enter a number: "))
    num2 = int(input("enter second number: "))
    operator = input("add, multiply, subtract or divide: ").lower()
    if operator == "add":
        add(num1, num2)
    elif operator == "multiply":
        multiply(num1, num2)
    elif operator == "subtract":
        subtract(num1, num2)
    elif operator == "divide":
        divide(num1, num2)
    else:
        print("invalid input")
    again = input("type y if you want to go again: ")
