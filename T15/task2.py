# T15 TASK 2 - LEAP YEAR CHECKER

# Prompts user to input the start year and how many years after that they would like to check
start_year = int(input("Enter the year you wish to start at:\n")) # Note: recasts as an integer (assumes user will enter a number else this is throw a ValueError)
number_of_years = int(input("How many years do you wish to check?\n"))

# Bars and title for presentability of output
print('─'*50)
print("LEAP YEAR CHECKER\n")

# Loops from start year incrementing after the required number of years has passed
for i in range(start_year,start_year + number_of_years):
    is_Not = "is" if i%4 == 0 else "is not" # If statement in shorthand one-line notation to produce substring for printed output
    print(f"The year {i} {is_Not} a leap year.") # Prints conclusion on one line whether that year is a leap year or not.
print('─'*50)
