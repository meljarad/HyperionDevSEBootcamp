#TASK 17 OPTIONAL TASK - PALINDROME CHECKER

# Prints border, title and description to the user for readability and UI purposes
print('─'*120, "\nPALINDROME CHECKER")
print("\nThis program will check if any word/sentence is a palindrome!")
print("This program is not case-sensitive, and works best if you exclude punctuation marks.")

# Prompts user to input a string; cleanses string of spaces and case
my_sentence = input("\nEnter a string below to begin:\n")
cleansed_sentence = my_sentence.lower().replace(" ","")

# Initialises counter for use in below loop
same_letter_count = 0

# For loop used to check if each ith letter and each (-i-1)th letter, incrementing the counter if condition is met
for i in range(0, len(cleansed_sentence)):
    if cleansed_sentence[i] == cleansed_sentence[-i-1]:
        same_letter_count += 1

# Prints a statement based on a comparison of whether the count of the letters that are the same is the same as the word length
result = "is a palindrome!" if same_letter_count == len(cleansed_sentence) else "is not a palindrome!"

print(f"\nResult:\n\'{my_sentence}\' {result}")
print('─'*120) # Prints border for readability and UI purposes
