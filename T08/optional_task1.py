# T07 OPTIONAL TASK 1 - ODD/EVEN CHECKER

# Prompt user to enter an integer
my_int = int(input("Enter any integer:\n"))
# Tests whether the integer is odd or even using shorthand one-line notation of if-else statement
condition = "even" if my_int%2 == 0 else "odd"
# Output to the user whether the integer is odd or even
print(f"You have entered number {my_int}, which is an {condition} number.")
