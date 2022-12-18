# T07 TASK 02 - FULL NAME

# Prompts user to input their full name and uses strip() to remove trailing/leading spaces in case of only one name entered as an additional QA
full_name = input("Please enter your full name:\n").strip()
# Use .split() function learned from previous lessons to check number of names entered as an additional QA
number_of_names = len(full_name.split(" "))

# The following code ensures that the appropriate output statements are only printed when two names are read
if number_of_names == 1: # User to prompted to check their input if they have entered just one name
    print("Are you sure you have entered your full name?")
elif len(full_name) == 0: # User to prompted to check their input if they have entered nothing
    print("You haven't entered anything. Please enter your full name.")
else: # If at least 2 names are found, the following conditions are executed
    if 0 < len(full_name) < 4:
        print("You have entered less than four characters. Please make sure you have entered your name and surname.")
    elif len(full_name) > 25:
        print("You have entered more than 25 characters. Please make sure you have only entered your full name.")
    else:
        print("Thank you for entering your name.")
