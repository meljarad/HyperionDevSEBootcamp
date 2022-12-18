#T20 - TASK 2 - COMBINED

# Declaration of initial variable set
integers_1 = []
integers_2 = []
i = 0
j = 0
border_length = 120

# Asks user to enter 5 integers of their choice to be written to "numbers1.txt" and stores all 5 integers in a list
print('─'*(round(border_length*0.75))) # Prints border for readability and UI purposes
print("FIRST INTEGER SET:")
while i < 5:
    integer = int(input(f"{i + 1}/5. Enter an integer to be sorted in the first file (\"numbers1.txt\"):\n"))
    integers_1.append(integer)
    i += 1

# Sorts the numbers entered by the user and appends them to a new file created called "numbers1.txt"
integers_1.sort()
for i in integers_1:
    with open("numbers1.txt", "a") as numbers1_txt:
        numbers1_txt.write(f"{i}\n")

# A confirmation message is then outputted to the user
print(f"The integers {integers_1} have been sorted and written to the first file (\"numbers1.txt\").\n")

# Asks user to enter 5 integers of their choice to be written to "numbers2.txt" and stores all 5 integers in a list
print('─'*(round(border_length*0.75))) # Prints border for readability and UI purposes
print("SECOND INTEGER SET:")
while j < 5:
    integer = int(input(f"{j + 1}/5. Enter an integer to be sorted in the second file (\"numbers2.txt\"):\n"))
    integers_2.append(integer)
    j += 1

# Sorts the second set of numbers entered by the user and appends them to a new file created called "numbers2.txt"
integers_2.sort()
for i in integers_2:
    with open("numbers2.txt", "a") as numbers2_txt:
        numbers2_txt.write(f"{i}\n")

# A second confirmation message is then outputted to the user
print(f"The integers {integers_2} have been sorted and written to the second file (\"numbers2.txt\").\n")

# Creates a new list that combines the first and second sets of integers, then sorts it
all_numbers = (integers_1 + integers_2)
all_numbers.sort()

# Appends the sorted list of combined numbers to a new file created called "all_numbers.txt"
for i in all_numbers:
    with open("all_numbers.txt", "a") as allnumbers_txt:
        allnumbers_txt.write(f"{i}\n")

# A final confirmation message is then outputted to the user
print(f"DONE!\nAll entered integers {all_numbers} have been sorted and written to the third file (\"all_numbers.txt\").")
print('─'*border_length) # Prints border for readability and UI purposes
