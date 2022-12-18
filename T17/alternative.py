#TASK 17 TASK 1 - ALTERNATIVE.PY

# Prompts user to input a string and declares an empty list (used later for building new word)
my_sentence = input("Enter a string below:\n")
alternating_case_per_char = []

# Loops through all characters in the sentence and determines if the index is odd or even
for i in range(0, len(my_sentence)):
    # If the index is even, it capitalises the element (i.e. the character), otherwise it assumes the index is odd and makes it lowercase.
    if i%2 == 0:
        alternating_case_per_char.append(my_sentence[i].upper())
    else:
        alternating_case_per_char.append(my_sentence[i].lower())

# The new sentence is constructed from the newly-converted characters in the list using the .join() function and restoring spaces
print(''.join(alternating_case_per_char))

# Prompts user to input a second string and creates a list containing only the words, using the space character as a delimiter
my_sentence2 = input("\nEnter another string below:\n")
alternating_case_per_word = my_sentence2.split(" ")

# Loops through all words in the sentence by looking at each element in the newly-created list and determines if the index is odd or even
for i in range(0, len(alternating_case_per_word)):
    # If the index is even, it capitalises the element (i.e. the word), otherwise it assumes the index is odd and makes it lowercase.
    if i%2 == 0:
        alternating_case_per_word[i] = alternating_case_per_word[i].lower()
    else:
        alternating_case_per_word[i] = alternating_case_per_word[i].upper()

# The new sentence is constructed from the newly-converted characters in the list using the .join() function and restoring spaces
print(' '.join(alternating_case_per_word))
