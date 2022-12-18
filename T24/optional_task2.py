# T24 - OPTIONAL TASK 2

# User-defined functions for addition, subtraction, multiplication and division operations respectively
def add_num(num1, num2):
    return num1 + num2

def subtract_num(num1, num2):
    return num1 - num2

def multiply_num(num1, num2):
    return num1*num2

def divide_num(num1, num2):
    return num1/num2

def output(num1, num2):
    if option_num == 1:
        calculation = add_num(num1, num2)
        symbol = ' + '
    elif option_num == 2:
        calculation = subtract_num(num1, num2)
        symbol = ' - '
    elif option_num == 3:
        calculation = multiply_num(num1, num2)
        symbol = '*'
    elif option_num == 4:
        calculation = divide_num(num1, num2)
        symbol = '/'

    return symbol, calculation

# Prompts user to input two numbers of their choice to be used in operation
number1 = float(input("Enter your first number:\n"))
number2 = float(input("Enter your second number:\n"))

# Prompts user to select operation of choice from the printed menu
print("Select the operation you would like to perform on the two entered numbers by typing the corresponding number from the below menu:")
option_num = int(input("\t1. Add\n\t2. Subtract\n\t3. Multiply\n\t4. Divide\n"))

# Performs relevant operation returning the result and the relevant symbol for output to user
result = output(number1, number2)
print(f"YOUR RESULT:\n{number1}{result[0]}{number2} = {result[1]}")
