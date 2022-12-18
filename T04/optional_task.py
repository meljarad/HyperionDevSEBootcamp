# User input casted as floats then recasted as integers to avoid potential rounding display issues and invalid literal error
num1 = int(float(input("Please enter your first integer:\n")))
num2 = int(float(input("Please enter your second integer:\n")))

# Effective numerical variable value swapping without need for declaring third variable using arithmetic operators, credit due to Sumit Sudhakar who provided the techqnue
# Sumit Sudhakar's original code can be found on https://www.geeksforgeeks.org/swap-two-numbers-without-using-temporary-variable/
num1 += num2 # Reassigns sum of num1 and num2 to num1, using num1 as a temporary variable
num2 = num1 - num2 # Reassigns difference of the 'new' num1 and num2 (equal to 'old' num1 value) back to num2
num1 -= num2 # Reassigns difference of the 'new' num1 and 'new' num2 (equal to 'old' num2 value) back to num1

print(f"Before the swap, the original integer values were 'num1' = {num2} and 'num2' = {num1}.")
print(f"After the swap, the new integer values are 'num1' = {num1} and 'num2' = {num2}.")
