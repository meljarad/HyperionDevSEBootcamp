# T16 TASK 2 - LOGIC.PY
# The below program is a prime number calculator that determines if a given number is a prime number or not.
# The program then uses the same technique to determine how many primes are smaller than that number, and displays them.
# The program has been intentionally coded to include a logical error, such that the second part of the output does the opposite function.
# The second part of the output prints everything smaller than the original number that is NOT a prime number when it should be showing ONLY primes.
# This logical error is due to line 30, where the '>' sign should be replaced with a '<=' in order to function as intended.

# Prints border, title and description to the user for readability and UI purposes
print('─'*110)
print("PRIME NUMBER CALCULATOR")
print("\nThis programme will check if any integer is a prime number, and list all prime numbers before it!")

# Takes in numeric value from user and recasts as an integer
my_integer = int(input("To begin, any positive integer:\n"))

# Checks if the user's number is a prime number by looping through all numbers before sequentially and storing factors in a list
my_integer_factors = []

for i in range(1, my_integer + 1):
    if my_integer%i == 0: my_integer_factors.append(i) # Any factors will be perfectly divisible with no remainder
    is_Prime = "is NOT" if len(my_integer_factors) > 2 else "IS" # Any non-prime will always have more than 2 factors

# Checks for all primes before the number by repeating the same technique on all numbers beforehand using a nested for loop
small_primes = []

for j in range(1, my_integer + 1):
    j_factors = []
    for k in range(1, j + 1):
        if j%k == 0: j_factors.append(k)
    if len(j_factors) > 2: small_primes.append(j)

small_primes.remove(small_primes[-1]) # Removes user's number from the list (which will always be last value)

# Prints a summary of the calculations to the user
print(f"\n{my_integer} {is_Prime} a prime number as it has {len(my_integer_factors)} factors:\n{my_integer_factors}")
print(f"\nThe number of prime numbers smaller than {my_integer} is equal to {len(small_primes)}. The list of prime numbers smaller than {my_integer} is:\n{small_primes}")
print('─'*110) # Prints border for readability purposes
