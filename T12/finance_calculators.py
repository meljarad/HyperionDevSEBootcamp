#T12 - CAPSTONE PROJECT I
# Note 1: assumed currency is in Rand hence all output values will append currency symbol 'R' before the value

import math # Allows for use of math.pow() functions through

# Prompts user to input selection by choosing either the investment calculator or bond repayment calculator
print("Choose either \'investment\' or \'bond\' from the menu below to proceed:\n")
print("investment\t–\tto calculate the amount of interest you\'ll earn on your investment")
print("bond\t\t–\tto calculate the amount of interest you\'ll have to pay on a home loan")
user_selection = input("").lower().strip() # Cleanses input by standardizing case and removing leading/trailing spaces
print('─'*90) # Boundary output for readability purposes

if user_selection == "investment": # Decision logic intended to perform investment return calculations based on user selected 'investment'
    # Prompts user to input starting variables (initial balance, annual interest rate, years to be invested)
    print("INVESTMENT RETURN CALCULATOR:\n")
    initial_balance = float(input("Enter the amount of money to be deposited:\nR"))
    annual_interest_rate = float(input("Enter your annual interest rate as a decimal (excluding the percentage sign):\n%"))/100
    years_invested = round(float(input("How many years do you plan to invest your money for?\n")))

    print("Choose either \'simple\' or \'compound\' interest from the menu below to proceed:\n")
    print(" simple\t\t–\tinterested accrued as a fixed percentage of the principal amount deposited")
    print(" compound\t–\tinterest accrued and added to the accumulated interest of previous periods, as well as principal amount\n")
    interest_type = input().lower().strip() # Note use of .lower() and .strip() to cleanse user input

    # Decision logic intended to perform correct calculations based on whether user wants simple or compounded interest
    if interest_type == 'simple':
        final_balance = initial_balance*(1 + annual_interest_rate*years_invested)
        yearly_interest_amount = initial_balance*annual_interest_rate
        interest_statement = f"Yearly interest amount:\t\tR{str(round(yearly_interest_amount,2))}" # Yearly interest amount to be printed with output
    elif interest_type == 'compound':
        final_balance = initial_balance*math.pow((1+annual_interest_rate),years_invested)
        annual_percentage_yield = math.pow((1 + (annual_interest_rate/years_invested)),years_invested) - 1
        interest_statement = f"Annual percentage yield:\t{str(round(annual_percentage_yield*100,2))}%" # Annual percentage yield to be printed with output
    else: # QA step included in case user types invalid entry. (Best thing to do would be to define the calculations and output as they're own functions and then run in their respective if statements to avoid NameError)
        print("ERROR! Invalid interest type selection. Please re-run program and select from the two options by either typing \'simple\' or \'compound\'")

    total_interest_accrued = final_balance - initial_balance # Supplementary information (total interest accrued) to be printed with output

    # Prints initially entered variables and calculated variables to user using tabs, line breaks and lines for readable output
    print('─'*90,"\nINVESTMENT RETURN CALCULATOR RESULTS:\n")
    print(f"Initial balance:\t\t\tR{initial_balance}")
    print(f"Interest rate applied:\t\t{annual_interest_rate*100}%")
    print(f"Years invested (rounded):\t{years_invested} years")
    print(f"Interest method applied:\t{interest_type.capitalize()} interest\n") # Note use of .capitalize() to output correct capitalization of sentence
    print(f"{interest_statement}")
    print(f"Total interest accrued:\t\tR{total_interest_accrued:.2f}\n")
    print(f"Final balance:\t\t\t\tR{final_balance:.2f}")
    print('─'*90)

elif user_selection == "bond": # Decision logic intended to perform bond repayment calculations based on user selected 'bond'
    # Prompts user to input starting variables (house value, monthly interest rate (derived from annual), months remaining)
    print("BOND REPAYMENT CALCULATOR:\n")
    house_present_value = float(input("Enter the present value of the house:\nR"))
    monthly_interest_rate = float(input("Enter your yearly interest rate as a decimal (excluding the percentage sign):\n%"))/100/12
    remaining_months_to_repay_bond = round(float(input("How many months do you plan to take to repay the bond?\n")))

    monthly_repayment = (monthly_interest_rate*house_present_value) / (1 - math.pow(1 + monthly_interest_rate,-(remaining_months_to_repay_bond)))

    # Prints initially entered variables and calculated variables to user using tabs, line breaks and lines for readable output
    print('─'*90,"\nBOND REPAYMENT CALCULATOR RESULTS:\n")
    print(f"House present value:\t\t\t\tR{house_present_value}")
    print(f"Monthly interest rate applied:\t\t{monthly_interest_rate*100}%")
    print(f"Planned number of months to repay:\t{remaining_months_to_repay_bond} months\n")
    print(f"Monthly amount to repay:\t\t\tR{monthly_repayment:.2f}")
    print('─'*90)
else:  # QA step included in case user types invalid entry
    print("ERROR! Invalid selection. Please re-run program and select from the two options by either typing \'investment\' or \'bond\'.")
