# T15 TASK 3

# *************************FIRST SUBTASK*************************
# The below code displays a countdown from 20 to 0 (inclusive)
print('─'*40,"\nSUBTASK 1: COUNTDOWN FROM 20 TO 0") # Bars and title for presentability of output
i = 20 # Declaration of upper boundary condition at 20

# Fulfils below conditions by declaring lower bound condition at 0
while i >= 0:
    print(i) # Output number to the user
    i-=1 # Decrement number by 1


# *************************SECOND SUBTASK*************************
# The below code displays all even numbers from 1 to 20 (inclusive)
print('─'*40, "\nSUBTASK 2: ALL EVEN NUMBERS FROM 1 TO 20") # Bars and title for presentability of output

# Uses a while loop with nested if statement designed to test parity using modulus function and skip odd numbers
for j in range(0,21):
    if j%2 == 0:
        print(j)
    else:
        continue


# *************************THIRD SUBTASK*************************
# The below code displays up to 5 asterisks using a for loop
print('─'*40,"\nSUBTASK 3: INCREMENTING ASTERISKS") # Bars and title for presentability of output

for i in range(1,6):
    print("*"*i,"\n") # Increases string length each time by multiplying the asterisk by the iterator


# *************************FOURTH SUBTASK*************************
# The below code calculates the greatest common divisor (GCD) of two integers
print('─'*40,"\nSUBTASK 4: GREATEST COMMON DIVISOR CALCULATOR") # Bars and title for presentability of output

# Prompts user to enter two positive integers (assumes user will enter a number else this is throw a ValueError)
integer1 = int(input("Enter the first positive integer of your choice:\n"))
integer2 = int(input("Enter the second positive integer of your choice:\n"))

# Declares two empty lists to be used for storing calculated divisors:
integer2_divisors = []
common_divisors = []

# One-line shorthand notation that ensures 'integer2' is always the smaller variable (makes for more efficient divisor determination, see below)
if integer2 > integer1: integer1, integer2 = integer2, integer1

# For-loop used to loop through all numbers from 1 to 'integer2' and determine and store its divisors
for i in range(1, integer2+1):
    if integer2%i == 0: integer2_divisors.append(i)

# For-loop used to loop through all divisors of 'integer2' and determine which are common divisors with 'integer1'
for j in range(0, len(integer2_divisors)):
    if integer1%integer2_divisors[j] == 0: common_divisors.append(integer2_divisors[j])

# Sorts common divisors and prints the greatest of them by choosing the final element
common_divisors.sort() # Technically this is not strictly necessary with my method but it's a good QA step
print(f"The greatest common divisor (GCD) of {integer1} and {integer2} is {common_divisors[-1]}.")
