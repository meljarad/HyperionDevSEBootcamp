#TASK 17 TASK 2 - SEPARATION.PY

# Prompts user to input a string and creates a list containing only the words, using the space character as a delimiter
my_sentence = input("Enter a string below:\n")
print(f"Your sentence is:\n {my_sentence}")

# Modifies the sentence using  the .replace() function to replace all space characters with a line break
my_sentence = my_sentence.replace(" ", "\n ") # A space is added after line breaks to indent the output for improved user readability

# Outputs to new modified sentence to the user
print(f"\nYour sentence contains the following words:\n {my_sentence}") # A space is added after line breaks to indent the output for improved user readability
