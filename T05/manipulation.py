# T05 TASK 3

# Prompts user to enter a sentence to be written to "str_manip"
str_manip = input("Please enter a sentence:\n")

# Calculates its length and then prints the length to the user
str_manip_length = len(str_manip)
print(f"\nThe length of your sentence is {str_manip_length} characters (including any spaces and punctuation).")

# Finds the last letter of "str_manip"
last_letter = str_manip[str_manip_length-1]

# Replaces the last letter of "str_manip" with the "@" character
str_manip_replaced = str_manip.replace(last_letter,"@")
print(f"\nIf all instances of the last character of your sentence are replaced with the \"@\" character, your sentence becomes:\n\"{str_manip_replaced}\"")

# Prints the last 3 characters in "str_manip" backwards
last_three_letters = str_manip[-1:-4:-1]
print(f"\nThe last three characters of your sentence backwards are:\n\"{last_three_letters}\"")

# Five letter word composed of the first three letters and last two letters of "str_manip'
five_letter_word = str_manip[0:3] + str_manip[-2:]
print(f"\nThe following word is created by using the first three letters and last two letters of your sentence:\n\"{five_letter_word}\"")

# Displays each word of "str_manip" on a new line
str_manip_new = "\n".join(str_manip.split(" "))
print(f"\nWhen all spaces are replaced with line breaks, your sentence looks like this:\n\"{str_manip_new}\"")
