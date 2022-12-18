# MENU PROGRAM
# This program prompts users to order three food items and then outputs the order back to the user to read.

print("Welcome! Order any three food items using the prompts below:\n") # Line breaks are employed to enhance user readibility in the output
item1 = str(input("What is the first food item you wish to order?\n")) # Use of str() converts input to string, preventing concatenation errors when printing out the order below
item2 = str(input("What is the second food item you wish to order?\n"))
item3 = str(input("What is the third food item you wish to order?\n"))

print("Order confirmed! You have ordered the following items:")
print("1. " + item1)
print("2. " + item2)
print("3. " + item3)
