# T16 OPTIONAL TASK
# The below program is a calculator that determines the average number of letters per word.
# The program asks the user for a sentence, counts the number of words and works out two averages (with and without spaces).
# The program has been intentionally coded to include a logical error, such that a runtime error is also triggered as a result in a specific instance.
# On line 18, notice that the word count is incorrectly decremented by 2.
#  This will trigger a runtime error for any sentence with only 2 words due to an attempt to divide by zero.
#  For any other word count not equal to two, a logical error will arise from incorrect results derived from an erroneously calculated word count.

# Prints border, title and description to the user for readability and UI purposes
#print('─'*100)
print("AVERAGE CHARACTERS PER WORD CALCULATOR")
print("\nThis programme will check any sentence to count how many average characters per word your sentence has!\n")

# Takes in a sentence from user
my_words = input("Enter a sentence of your choice:\n")

# Calculates the number of average number of characters per word with and without spaces
word_count = len(list(my_words.split())) - 2
char_count_incl_spaces = len(my_words)
char_count_excl_spaces = len(my_words.replace(" ", ""))
average_word_length_excl_spaces = round(char_count_excl_spaces/word_count, 3)
average_word_length_incl_spaces = round(char_count_incl_spaces/word_count, 3)

# Prints a summary of the calculations to the user
print("\nSUMMARY STATISTICS:")
print('─'*100) # Prints border for readability purposes
print("Your sentence:" + "\t"*12 + f"\'{my_words}\'")
print("Total number of words:" + "\t"*10 + f"{word_count} word(s)")
print(f"Average number of characters per word excluding spaces:" + "\t"*2 + f"{average_word_length_excl_spaces} character(s) per word")
print(f"Average number of characters per word including spaces:" + "\t"*2 + f"{average_word_length_incl_spaces} character(s) per word")
print('─'*100) # Prints border for readability purposes
