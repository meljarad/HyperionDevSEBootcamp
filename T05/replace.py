# REPLACE PROGRAM

my_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
my_string2 = (my_string.replace("!"," "))[:-2] + "." # This line replaces the excalamation marks with spaces, trims the final two characters " ." and concatenates with a full stop without a space instead so that the string exactly reflects the string requested in the task brief.
my_string3 = my_string2.upper() # Converts second string all to upper case
my_string4 = my_string3[::-1] # Flips the third string so it is written in reverse from the last character

# Subsequent output to user using new lines for user readability
print(f"String 1 (Original): \n\"{my_string}\"\n")
print(f"String 2 (Exclamation marks replaced with spaces): \n\"{my_string2}\"\n")
print(f"String 3 (Capitalised version of string 2): \n\"{my_string3}\"\n")
print(f"String 4 (Reversed version of string 3 statement): \n\"{my_string4}\"")
