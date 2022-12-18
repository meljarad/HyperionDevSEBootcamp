# T23 - TASK 1 - FLOAT MANIPULATION

import math # Allows for use of various mathematical functions

# Initial declaration of important variables used below to store entered numbers
num_count = 0
num_list = []
cumulative_total = 0

# Prints top border, title and description to the user for readability and UI purposes
border_length = 100
print('─'*border_length, "\n10-NUMBER MATHS")
print("This program will ask you for 10 numbers and then will give you some summary statistics about them!\n")

# Prompts user to enter 10 different numbers and stores them in num_list
while num_count < 10:
    my_num = float(input(f"{num_count + 1}/10: Enter any number:\n"))
    num_list.append(my_num)
    cumulative_total += my_num # Used to calculate the running total of all numbers entered, avoiding need for another loop
    num_count += 1

# Calculates the highest number out of all entered numbers and finds its index value
maximum_number = max(num_list)
maximum_number_index = num_list.index(maximum_number)

# Calculates the lowest number out of all entered numbers and finds its index value
minimum_number = min(num_list)
minimum_number_index = num_list.index(minimum_number)

# Calculates the mean (average) of all entered numbers and rounds it off to 2 decimal places
mean_2dp = round(cumulative_total/len(num_list), 2)

# Derives the median using the highest and lowest numbers
median = (maximum_number + minimum_number)/2

# A summary of the above calculate variables is printed back to the user
print('─'*border_length)
print(f"SUMMARY STATISTICS:\n\nYou have entered the following numbers:\n{num_list}")
print(f"\nDid you know that...\n\t-The total of all numbers entered is {cumulative_total}")
print(f"\t- The highest number of all numbers entered is {maximum_number} and is found at index value {maximum_number_index}")
print(f"\t- The lowest number of all numbers entered is {minimum_number} and is found at index value {minimum_number_index}")
print(f"\t- The mean of all numbers entered (to 2 decimal places) is {mean_2dp:.2f}")
print(f"\t- The median of all numbers entered is {median}")
print('─'*border_length) # Prints bottom border for UI purposes
