#T14 - TASK 1, EVEN.PY

# Prompts the user to enter any number
i = 1
my_number = float(input("Enter a number:\n")) # Assumes user will input a numeric, code will break if string is entered

if my_number < 1: # Checks if a number less than 1 has been entered
    print(f"ERROR: {my_number} is less than 1! Please rerun program and enter a positive number.")
else:
    if my_number.is_integer() == False: # If a decimal number has been entered, it will be rounded to the nearest whole number and recasted as an int
        print(f"{my_number} has been rounded to the nearest integer, {round(my_number)}.")
        my_number = int(round(my_number))
    # All even numbers from 1 up to and including the entered number will then be printed to user:
    print(f"All even numbers from 1 up to and including {int(my_number)} are:")
    while i <= my_number:
        if i%2 == 0: print(f"{i}") # Checks if iterator is even using modulus function and prints if so, written using shorthand one line notation
        i+=1
