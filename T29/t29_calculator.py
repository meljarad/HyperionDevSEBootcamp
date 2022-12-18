# T29 - TOWARDS DEFENSIVE PROGRAMMING - T29_CALCULATOR.PY

import datetime # Used to record the timestamp of calculation

# Custom-defined function that allows for user-input of operands and operator selection
def go_to_main_menu():
    global border_length

    print('─'*border_length, "\nSIMPLE CALCULATOR")
    print("\nThis simple program will ask you for two numbers and then perform your chosen mathematical operation on them.\n")
    print("Select one of the following two options by typing \'1\' or \'2\':")
    print("\t1. Perform a simple calculation based on user-inputted numbers and operation.")
    print("\t2. Import a list of equations from a text-file and print out the results.\n")

    while True:
        try:
            user_menu_choice = int(input("Enter your selection:\n"))
            break
        except ValueError:
            print("Error: Invalid value, please only enter numerical values.")

    while user_menu_choice not in [1, 2]:
        print("Error: Invalid value, please only select 1 or 2.")
        while True:
            try:
                user_menu_choice = int(input("Enter your selection:\n"))
                break
            except ValueError:
                print("Error: Invalid value, please only enter numerical values.")

    if user_menu_choice == 1:
        simple_calculation()
    elif user_menu_choice == 2:
        import_equations_from_file()
        compute_imported_equations()

# Performs a simple operation based on two user-inputted operands and a chosen operator
def simple_calculation():
    global num_1
    global num_2
    global chosen_operator

    # Enter first operand - try-except block used to ensure non-numerical values are not entered
    while True:
        try:
            num_1 = float(input("Enter a first number:\n"))
            break
        except ValueError:
            print("Error: Invalid value, please only enter numerical values.")

    # Enter second operand - try-except block used to ensure non-numerical values are not entered
    while True:
        try:
            num_2 = float(input("Enter a second number:\n"))
            break
        except Exception:
            print("Error: Invalid value, please only enter numerical values.")

    # Restricts operation to only acceptable values
    while True:
        acceptable_operations = ['+', '-', '/', 'x', 'add', 'subtract', 'divide', 'multiply']
        print("Select your chosen mathematical operation:")
        print("\t1. Addition: type \'+\' or \'add\'")
        print("\t2. Subtraction: type \'-\' or \'subtract\'")
        print("\t3. Division: type \'/\' or \'divide\'")
        print("\t4. Multiplication: type \'x\' or \'multiply\'")
        chosen_operator = input("")
        if chosen_operator not in acceptable_operations:
            print("Error: Invalid selection. Please try again.")
        else:
            break

    # Perform relevant calculation based on user-inputs and prompt user to exit or return to main menu
    decision_logic(chosen_operator, num_1, num_2)
    menu_or_exit()

# Custom-defined function that allows for writing output of calculation to a text file
def write_equation_to_file(equation):
    global calculation_num
    global formatted_time

    with open("calculation_history.txt", "a") as f:
        f.write(f"Calculation {calculation_num} performed at {formatted_time}:\n" + equation + "\n")

# Custom-defined function that when called allows user to return to main menu or end program
def menu_or_exit():
    global border_length
    user_selection = input("\nPress enter to go back to main menu or type 'e' to exit:\n")
    if user_selection == 'e':
        print("Program successfully terminated.")
        with open("calculation_history.txt", "a") as f:
            f.write(f"\nProgram successfully terminated at {formatted_time}.\n")
        exit()
    elif user_selection == '':
        go_to_main_menu()
    else:
        print("Error: Invalid selection.")
        menu_or_exit()

# Custom-defined function that will add two user-inputted operands together and write calculation to a file
def addition_operation(operand_1, operand_2):
    global calculation_num
    result = operand_1 + operand_2
    equation = f"{operand_1} + {operand_2} = {result}"
    print(f"Calculation {calculation_num}:\n" + equation)
    write_equation_to_file(equation)
    calculation_num += 1

# Custom-defined function that will subtract two user-inputted operands together and write calculation to a file
def subtraction_operation(operand_1, operand_2):
    global calculation_num
    result = operand_1 - operand_2
    equation = f"{operand_1} - {operand_2} = {result}"
    print(f"Calculation {calculation_num}:\n" + equation)
    write_equation_to_file(equation)
    calculation_num += 1

# Custom-defined function that divide two user-inputted operands together and write calculation to a file
def division_operation(operand_1, operand_2):
    global calculation_num
    result = operand_1/operand_2
    equation = f"{operand_1} ÷ {operand_2} = {result}"
    print(f"Calculation {calculation_num}:\n" + equation)
    write_equation_to_file(equation)
    calculation_num += 1

# Custom-defined function that will multiply two user-inputted operands together and write calculation to a file
def multiplication_operation(operand_1, operand_2):
    global calculation_num
    result = operand_1*operand_2
    equation = f"{operand_1} × {operand_2} = {result}"
    print(f"Calculation {calculation_num}:\n" + equation)
    write_equation_to_file(equation)
    calculation_num += 1

# Custom-defined function that uses conditional logic to determine which operation to use based on use input
def decision_logic(operator, operand_1, operand_2):
    global calculation_num
    if (operator == "+") or (operator == 'add'):
        addition_operation(operand_1, operand_2)
    elif (operator == "-") or (operator == 'subtract'):
        subtraction_operation(operand_1, operand_2)
    elif (operator == "/") or (operator == 'divide'):
        division_operation(operand_1, operand_2)
    elif (operator == "x") or (operator == 'multiply'):
        multiplication_operation(operand_1, operand_2)
    else:
        print("Error: invalid selection.")
    menu_or_exit()

# Reads equations from a user-specified file, parses them and stores in a list for further computation
def import_equations_from_file():
    global equation_list_final_parsable
    global rejected_equations
    # Notifies user of how the file to import equations from should be listed
    print("Notes - PLEASE READ BEFORE IMPORTING:")
    print("- File should contain one equation per line, containing two operands and one operator")
    print("- No delimiters except spaces should be used to separate the operands with the operator in-between (e.g. \'seven times eight\' should be represented as \'7 x 8\' or \'7x8\')")
    print("- The equation should not include any equals symbols (i.e. lines should not end with \'=\')")
    print("- Operands should be numerical values only. Equations containing non-numerical operands will be discarded.")
    print("- Operator symbols should be represented using only the following characters:")
    print("\t\'+\' used as the addition operator (i.e. to add two numbers together)")
    print("\t\'-\' used as the subtraction operator (i.e. to subtract two numbers together)")
    print("\t\'*\' used as the multiplication operator (i.e. to multiply two numbers together)")
    print("\t\'/\' used as the division operator (i.e. to divide one number by another)\n")

    # Ask the user to input which file they should be extracting
    while True:
        file_name_to_read = input("Please enter the file name (case-sensitive) you wish to use to import equations, including the file extension (.txt) at the end:\n")
    # Create an empty list to store the equations extracted from the file
        equation_list = []
    # Open the file with a with-as block
        try:
            with open(file_name_to_read, 'r') as f:
                equation_list = f.readlines()
                break
        except FileNotFoundError:
            print("Error: File not found. Please try again.")
    # Strip newlines and remove all spaces from each line
    equation_list = [equation.replace(" ", "").strip() for equation in equation_list]
    print(f"Equations imported from file:")
    for equation in equation_list: print(equation)
    print("\nParsing equations...")


    # Rejects and removes equations that have more than two operands
    rejected_equations = []
    for equation in equation_list:
        num_operators = len([c for c in equation if c in '+-*/']) # Count the number of mathematical operators in the equation
        if num_operators > 1: # If there is more than one operator, add the equation to the rejected list
                rejected_equations.append(equation)
                equation_list.remove(equation)

    # Formats the prefinal list of equations to be parsed in the format [first operand, operator and second operand] using the operator as a delimiter
    valid_operators = ['+', '-', '/', '*']
    equation_list_prefinal = []
    for equation in equation_list:
        for delimiter in valid_operators:
            if delimiter in equation:
                equation_as_sublist = [equation.split(delimiter)[0], delimiter, equation.split(delimiter)[1]]
                equation_list_prefinal.append(equation_as_sublist)

    ## CODE WORKS GREAT UP TO HERE
    # Final cleansing step to ensure that the imported equations can be appropriately parsed by ensuring the operands are numeric
    equation_list_final_parsable = []
    for i in equation_list_prefinal:
        string_count = 0
        for j in i:
            # Converts all numbers in the equations to floats so they can be parsed later whilst preserving other characters as strings
            if j.isnumeric() == True:
                j = float(j)
            # Checks number of non-numeric items and rejects equation on assumption that there are more than two operands or more than one operator
            elif j.isnumeric() == False:
                string_count += 1
        # Store final list of "cleansed" equations in the final parsable list else place them in the rejected equations list
        if string_count == 1:
            equation_list_final_parsable.append(i)
        else:
            rejected_equations.append(" ".join([str(element) for element in i]))

    print(f"\nSuccessfully parsed equations:")
    for equation in equation_list_final_parsable: print("".join(equation))

    print(f"\nRejected equations:")
    for equation in rejected_equations: print(equation.replace(" ", ""))

def compute_imported_equations():
    global equation_list_final_parsable
    global rejected_equations

    print("\nComputing successfully parsed equations...\n")

    # Loops through the cleansed list of equations
    for equation in equation_list_final_parsable:
        # Extracts first and second operands and the operator
        first_operand = float(equation[0])
        second_operand = float(equation[2])
        operator_to_use = equation[1]

        # Decision logic to execute right operation based on extracted operator
        if operator_to_use == '+':
            addition_operation(first_operand, second_operand)
        elif operator_to_use == '-':
            subtraction_operation(first_operand, second_operand)
        elif operator_to_use == '/':
            division_operation(first_operand, second_operand)
        elif operator_to_use == '*':
            multiplication_operation(first_operand, second_operand)

    print(f"\nCalculation of {len(equation_list_final_parsable)}/{len(equation_list_final_parsable) + len(rejected_equations)} imported equation(s) successfully completed.")

    # Prints the list of equations that were not calculated due to rejection/failure to parse (i.e. more than one operator/two operands)
    print("\nThe following equations were imported but failed to parse due to presence of more than 2 operands or non-numeric operands:")
    for i in rejected_equations:
        print(i.replace(" ", ""))
    # Prompt user to return to main menu or exit
    menu_or_exit()

# Global variables defined for use throughout
border_length = 65 # Used for UI and readability purposes
## Time variables used for producing timestamps in user-readable format
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%H:%M:%S, %d-%b-%Y")

calculation_num = 1 # Initialisation of number of calculations

# Records start of program in text file when program is first run
with open("calculation_history.txt", "a") as f:
    f.write(f"{'─'*border_length}\nProgram successfully started at {formatted_time}.\n\n")

go_to_main_menu() # Allows user to begin from main menu
