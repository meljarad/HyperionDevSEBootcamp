#T31 - TASK 2 - METHOD OVERRIDE

# Class defined to model adults as objects
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    # Method that checks if a person is old enough to drive or not and prints conclusion to user
    def can_drive(self, name, age):
        print(f"As a {self.age} year old, {self.name} is old enough to drive as they over 18 years old.")

# Class defined to model children as objects
class Child(Adult):
    def can_drive(self, name, age):
        print(f"{self.name} is not old enough to drive as they are only {self.age} years old!")
# User is prompted to enter the person name
name = input("Enter the person's name:\n")

# User is prompted to enter the person age
while True:
    try:
        age = int(input("Enter the person's age:\n"))
        break
    except ValueError: # Prevents user from entering a non-integer (i.e. str/float) value for age
        print("Error: invalid value. Please only enter integer values for age.")

# User is prompted to enter the person hair colour
while True:
    try:
        hair_colour = input("Enter the person's hair colour:\n")
        float(hair_colour) # Convert entry to float and print error if type conversion is successful
        print("Error: invalid value. Please only enter non-numeric string values for hair colour.")
    except ValueError:
        # If type conversion to float is not successful, exit block as user has entered a string
        break

# User is prompted to enter the person eye colour
while True:
    try:
        eye_colour = input("Enter the person's eye colour:\n")
        float(eye_colour) # Convert entry to float and print error if type conversion is successful
        print("Error: invalid value. Please only enter non-numeric string values for eye colour.")
    except ValueError:
        # If type conversion to float is not successful, exit block as user has entered a string
        break

# Decision logic to determine if person is adult or child and calls correct class to construct appropriate object
if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)

# Print whether the person can drive or not by calling the appropriate method
person.can_drive(name, age)
