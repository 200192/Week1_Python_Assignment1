# This is a basic Calculator Program

# Ask the user to enter first number
num1 = int(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = int(input("Enter the second number: "))

# Ask the user to enter the operation
operation = input("Enter an operation (+, -, *, /): ")

# This is to perform the operation and display results
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
