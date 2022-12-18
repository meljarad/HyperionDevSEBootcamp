#TASK 17 TASK 3 - DISSAPPEAR.PY

# Prompts user to input a string and the characters they'd like to strip (separated using the comma as a delimiter)r
my_sentence = input("Enter a string below:\n")
characters_to_strip = input("Enter the characters you'd like to strip separating each one with a comma:\n")

# Remove the comma delimiter and splits characters to be stripped in to a list
characters_to_strip = characters_to_strip.split(",")

# Informs the user of the characters that will be stripped to by printing the list
print(f"\nThe following character(s) will be stripped from the original string:\n{characters_to_strip}")

# Compares each character to strip by checking if it's in the original sentence and remove it using the .replace() function
for i in characters_to_strip:
        if i in my_sentence: my_sentence = my_sentence.replace(i, "")

# Outputs the newly modified sentence with the chosen characters stripped
print(f"\nThe new stripped sentence is:\n{my_sentence}")
