# NUMBERS.PY T06 TASK 1

# Asks the user to input three different integers
int1 = int(input("Enter your first integer:\n"))
int2 = int(input("Enter your second integer:\n"))
int3 = int(input("Enter your third integer:\n"))

# Print out the sum of all three numbers
print(f"\nThe sum of the integers {int1}, {int2} and {int3} is equal to {int1 + int2 + int3}.")
# Print out the first number minus the second number
print(f"The value of {int1} - {int2} is equal to {int1 - int2}.")
# Print out the third number multiplied by the first number
print(f"The product of {int3} and {int1} is equal to {int3 * int1}.")
# Print out the sum of all three numbers divided by the third number
print(f"The sum of the integers {int1}, {int2} and {int3} divided by the integer {int3} equal to {(int1 + int2 + int3)/int3}.")
