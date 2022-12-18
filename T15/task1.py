# T15 TASK 1

# Takes user input and recasts as an integer (assumes user will enter a number else this is throw a ValueError)
my_int = int(input("Enter the integer of your choice:\n"))
end_int = int(input("Enter the size of your times table:\n"))

# Prints output to user in readable format using title, line breaks and borders for readability purposes
print('─'*20)
print(f"MULTIPLICATION TABLE\n\nThe {my_int} times table up to the multiple {end_int} is as follows:\n")

# Prints out the equation of the integer multiplied by the iterator up until the iterator is equal to table size
for i in range(1,end_int + 1):
    print(f"{my_int} x {i} = {my_int*i}")
print('─'*20)
