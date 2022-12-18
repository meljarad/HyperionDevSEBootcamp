# T10 - TASK 1
# Prompts user to input their age
age = int(input("Please enter your age:\n"))

# If-else if-else statement use conditional logic to determine the user's BMI status based on their BMI value
if age >= 18:
    print("You are old enough!")
elif 16 < age < 18:
    print("Almost there.")
else:
    print("You're just too young!")
