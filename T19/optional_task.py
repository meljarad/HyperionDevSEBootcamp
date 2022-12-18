# T19 OPTIONAL TASK

# Prints border, title and description to the user for readability and UI purposes
print('─'*110, "\nLINE, WORD AND CHARACTER COUNTER")
print("\nThis program will read the \"input.txt\" file and count how many words, lines and characters are present!")
print("Note: This program will include a count of empty lines, punctuation marks and special characters.")

# Uses with-as block to read all lines from "input.txt", write each line as an element of script_lines, then closes file
with open("input.txt", "r") as script_file:
    script_lines = [line.rstrip() for line in script_file]

# Declaration of counter variables
inclusive_line_count = len(script_lines)
exclusive_line_count = 0
word_count = 0
char_count = 0

# Iterates through the script line by line and counts the length of each line
for i in script_lines:
    char_count += len(i)
    if len(i) != 0:
        word_count += len(i.split(' ')) # Ensures empty lines are not counted as words
    else:
        exclusive_line_count += 1 # Allows for exclusion of empty lines from line count

exclusive_line_count = inclusive_line_count - exclusive_line_count # Updates exclusive line count

# Non-essential to task but extracts the title, author and chapter name by evaluating text after the 1st, 2nd, 3rd colons
title = (script_lines[0].split(":"))[1].strip()
author_name = (script_lines[1].split(":"))[1].strip()
chapter = (script_lines[2].split(":"))[1].strip()

# Prints output to the user using a border and tabs for better readability/UI
print("\nTitle:", "\t"*11, f"{title.upper()}")
print("Author:", "\t"*10, f"{author_name.upper()}""")
print("Chapter:", "\t"*10, f"{chapter.upper()}""")
print("\nNumber of lines (including empty lines)", "\t"*2, f"{inclusive_line_count} LINES")
print("Number of lines (excluding empty lines)", "\t"*2, f"{exclusive_line_count} LINES")
print("Number of words:", "\t"*8, f"{word_count} WORDS")
print("Number of characters:", "\t"*7, f"{char_count} CHARACTERS")

print('─'*110) # Prints border for readability and UI purposes
