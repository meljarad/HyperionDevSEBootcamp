# T15 OPTIONAL TASK
# Prompts user to input an integer which is then recast as an int
num = int(input("Enter an integer of choice:\n")) # Note: assumes user will enter a number else this is throw a ValueError

# Used to print the entered integer N times where N = 'num' assuming condition has been met ('num' > 10)
if num > 10:
    print(f"The number {num} will be printed {num} times:")
    for i in range(0, num): print(f"{num} (Line {i+1})") # Loop written in one line shorthand notation to output numbers
else:
    print("Sorry, too small.") # Outputs alternative message to user if 'num' is lower than 10
