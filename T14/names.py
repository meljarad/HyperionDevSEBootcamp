#T14 - TASK 2, NAMES.PY

# Initial variable declaration for use in loop
i = 0
pupil_name = ""
pupils = []

# While loop is used to run as many times as the user wishes before they stop the program
while pupil_name.lower().strip() != "stop": # Note use of .lower() and .strip() to cleanse "stop" entry
    pupil_name = input(f"Enter the name of pupil #{i+1}, or type \'Stop\' once all names have been entered):\n")
    pupils.append(pupil_name)
    i+=1 # Used to count names

# Print count of names to user as specified
print(f"The total number of names that has been entered is {i-1}. The names in order of entry are as follows:")

# Prints list of pupils; not essential to task but a nice extra!
for j in range(0,i-1):
    print(f"{j+1}. {pupils[j]}")
