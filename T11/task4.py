# T11 - COMPULSORY TASK 4

# Prompts user to input an integer
my_int = int(input("Enter an integer:\n"))

# Decision logic using conditional if statements to determine if the integer is divisble by 2 and/or 5, printing the conclusion to the user
if (my_int%2 == 0) and (my_int%5 == 0):
    print(f"Your integer, {my_int} is divisible by 2 and 5.")
elif (my_int%2 == 0) or (my_int%5 == 0):
    if (my_int%2 == 0):
        print(f"Your integer, {my_int} is divisible by 2 but not 5.")
    elif (my_int%5 == 0):
        print(f"Your integer, {my_int} is divisible by 5 but not 2.")
else:
    print(f"Your integer, {my_int} is not divisible by 2 or 5.")
