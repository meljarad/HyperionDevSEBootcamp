#T18 TASK 3 - JOHN.PY

# Initial declaration of blank string and list
my_sentence = ''
incorrect_names = []

# Repeatedly asks user to enter a name until and records entry in the list, until "John" is entered. Entry validated using if-statement.
while my_sentence != 'John':
    my_sentence = input("Enter your name: ")
    if my_sentence != 'John': incorrect_names.append(my_sentence)

# Outputs the list of incorrect names to the user
print(f"Incorrect names: {incorrect_names}")
