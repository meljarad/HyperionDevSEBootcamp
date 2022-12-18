# T24 - TASK 1 - MY_FUNCTION.PY

# User-defined function to print days of week by looping through a list containing them, via a for loop
def days_of_the_week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(f"The days of the week are:")
    for i in days: print(i)

# User-defined function to replace every second word in any sentence (taken in as a parameter) with the word "Hello"
def replace_with_hello(my_sentence_words):
    # Determines whether word is second word or not by looping through all of them and checking parity of index
    for i in range(0, len(my_sentence_words)):
        if i%2 != 0: my_sentence_words[i] = 'Hello'
    my_sentence_new = " ".join(my_sentence_words) # Reconstructs new second with replacements "Hello"
    print(f"\nYour new sentence is:\n{my_sentence_new}")


# Prints top border, title and description to the user for readability and UI purposes
border_length = 100
print('─'*border_length, "\nDAYS OF THE WEEK GENERATOR")
print("This program will print the days of the week by calling a user-defined function!\n")

days_of_the_week() # Calls first user-defined function to print days of the week, see function def above for more detail

# Prints top border, title and description to the user for readability and UI purposes
border_length = 100
print('─'*border_length, "\nCUSTOM SENTENCE GENERATOR")
print("This program will replace every second word of any sentence of your choice with the word \'Hello\'!\n")

# Prompts user to input a sentence of their choice and records each word as an element of a list by splitting based on space delimiter
my_sentence = input("Enter any sentence below:\n")
my_sentence_words = my_sentence.split(" ")

replace_with_hello(my_sentence_words) # Calls second user-defined function to print new sentence, see function def above for more detail

print('─'*border_length) # Prints bottom border for readability and UI purposes
