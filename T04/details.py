# Prompts user input for details around name, age and address
user_name = input("Please enter your name:\n") # Prompts user for name and casts as string
user_age = int(input("Please enter your age in years:\n")) # Prompts user for age and casts as integer
user_house_no = int(input("Please enter your house number:\n")) # Prompts user for house number and casts as integer
user_street_name = input("Please enter the name of your street:\n") # Prompts user for street name and casts as string

# Reprints the details in a concatenated output
print(f"{user_name} is {user_age} years old and lives at {user_house_no} {user_street_name}.")
