# HELLO WORLD PROGRAM
# This program employs basic input and print statements to demonstrate basic Python input/output functionality.

name = str(input("What is your name?\n")) # Use of str() ensures conversion of input to string, preventing concatenation errors when printing out below
print("Your name is " + name + ".")
age = int(input("What is your age?\n")) # Use of int() constrains the age as an integer. This is good practice as it preserves the intended type of 'age' incase 'age' is to be used elsewhere in the program.
print("Your name is {} and your age is {} years old.".format(name,age))
print("Hello World!")
