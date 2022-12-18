#T14 - OPTIONAL TASK
i = 101 # Initial declaration of value greater than hundred to use as condition in while loop

# While loop will execute so long as i is greater than 100
while i > 100:
    my_number = int(input("Enter an integer less than or equal to 100:\n")) # Prompt user to input a number
    # Conditional logic used to prompt user to re-enter a number in case of invalid entry (i.e. greater than 100)
    if my_number > 100:
        print("Oops! It looks like you entered a number greater than 100. Try again.")
        continue
    i = my_number # Allows for exiting of while loop by comparing conditional "i" to "my_number"

# Used to store original entry for sake of readability (see final print)
original_number = my_number

# If the entered number is 0, the number is to be multiplied by 2 else if it is odd it is to be multiplied by 3
if my_number%2 == 0:
    multiplier = 2
    parity = "even"
else:
    multiplier = 3
    parity = "odd"

# Multiplication is enacted and final output is printed to user
my_number *= multiplier
print(f"{original_number} is an {parity} number. {original_number} multiplied by {multiplier} is equal to {my_number}")
