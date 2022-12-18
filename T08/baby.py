# T07 TASK 01 - BABY

# Prompts user to enter their year of birth
year_of_birth = int(input("Enter your year of birth:\n"))
# A lazy way to code would be to just type in "2022 - year_of_birth" but we are so close to 2023 that this method was worth including. This year is a time-dependent variable and the user should be able to change it once incase it is decided to be used elsewhere throughout. A more effective method would be to extract the year from today's date using a datetime library however.
current_year = 2022
# This is of course a simplistic assumption to demonstrate the "if" statement's functionality. The variable "age" can be better thought of as the age they are OR will become by the end of the year.
age = current_year - year_of_birth
# Simple if condition to check if the "age" is equal to or greater than 18.
if age >= 18:
    print(f"Your age is {age}. Congrats you are old enough.")
