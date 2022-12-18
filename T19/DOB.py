#T19 TASK 1

# Initial variable declaration
file_contents = open("DOB.txt", "r")
names = []
dates_of_birth = []

# Reads from the text file interpreting each text line as a list
with open("DOB.txt", "r") as file_contents:
    full_text_lines = file_contents.readlines()

# Prints out each line as it is shown in the file, in the format specified by the task brief
# To see code to print only names, see final code block
print("Name")
for i in full_text_lines:
    i = i.rstrip() # Removes the trailing line break at the end of each line
    print(i)
    i = i.split(" ") # Turns each line into a "sub" list of the words by splitting on the space delimiter (done for further manipulation)
    dates_of_birth.append(' '.join(i[-3:])) # Reconstructs date of birth by joining last three words and storing in list

# Prints out dates of birth on each line in the format specified by the task brief
print("\nBirthdate")
for i in dates_of_birth: print(i)

# If you just want to print the names and not the date of birth included next to the name, use the names list via "for i in names: print(i)"
for i in full_text_lines:
    i = i.rstrip().split(" ")
    names.append(' '.join(i[0:2]))

