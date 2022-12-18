#T14 - TASK 3, WHILE.PY

# Declaration of initial variables for use in while loop
my_number = 0
numbers_list = []

# While loop used to repeatedly prompt user to enter a number until they enter -1 (Note: this assumes the user will input a number and will throw a ValueError if a string is entered)
while my_number != -1:
    my_number = float(input("Enter a number:\n"))
    numbers_list.append(my_number)

# Calculates average by excluding last element (-1) and prints output to user
average = sum(numbers_list[:-1])/(len(numbers_list)-1)
print(f"The average of the numbers {numbers_list[:-1]} is equal to {round(average,4)}.") # Rounds displayed average to 4 decimal places at most for simplicity and readability
