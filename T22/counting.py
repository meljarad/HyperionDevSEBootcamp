# T22 - TASK 3 - COUNTING.PY

# Prompts user to input any string of their choice
my_string = input("Enter any string below:\n")

# Creates a list of unique letters by representing them as keys in newly-created dictionary, with default values = 0
my_string_letters_dict = dict.fromkeys(list(my_string), 0)

# Declaration of character count iterator to be used in below loops
char_count = 0

# Iterates through unique letters, compares them to each string letter and increments character count if they're the same
for i in my_string_letters_dict:
    for j in my_string:
        if i == j:
            char_count += 1
    my_string_letters_dict.update({i : char_count}) # Updates the value of the unique letter with the final character count
    char_count = 0 # Resets the character count before moving on to the next unique letter

# Result is outputted to the user
print(f"\nThe final count of each unique character in the string is shown the below dictionary:\n{my_string_letters_dict}")
