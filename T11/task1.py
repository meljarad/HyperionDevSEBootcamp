# T11 - COMPULSORY TASK 1

# Prompts user to input three integers
num1 = int(input("Enter your first integer:\n"))
num2 = int(input("Enter your second integer:\n"))
num3 = int(input("Enter your third integer:\n"))

# Compares first and second integers and outputs statement showing which is larger
if num1 > num2:
    print(f"The first integer, {num1} is larger than the second integer, {num2}.")
elif num2 > num1:
    print(f"The second integer, {num2} is larger than the first integer, {num1}.")
else:
    print("Both numbers are equal.")

# If statement to check parity of first integer, written in one-line shorthand notation
print(f"The first integer, {num1} is even.") if num1 % 2 == 0 else print(f"The first integer, {num1} is odd.")

# Listing numbers from largest to smallest such that num1 is always largest, num2 is second and num3 is smallest
if num2 > num1: num1, num2 = num2, num1 # 'Sorts' first and second integer by swapping if second is larger than first
if num3 > num1: num1, num3 = num3, num1 # 'Promotes' third integer to first if is larger than 'num1 = current largest'
if num3 > num2: num3, num2 = num2, num3  # 'Sorts' remaining two integers by swapping the smaller with the larger

print(f"The numbers listed in descending order are: {num1}, {num2}, {num3}.")
