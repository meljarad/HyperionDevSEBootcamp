# T24 - OPTIONAL TASK 1

# Defines a function that allows for calculating the mean (average) of a list of numbers to 1 decimal place
def average(list_of_numbers):
    i = 0
    total = 0
    for i in list_of_numbers:
        total += i
    average = round(total/len(list_of_numbers), 1)
    return average

# Defines a function that allows for calculating the minimum number of a list of numbers
# Note: whilst the task specifies this function be defined as 'min', this causes a recursion error and so I have renamed to minimum
def minimum(list_of_numbers):
    return min(list_of_numbers)

# Defines a function that allows for calculating the maximum number of a list of numbers
# Note: whilst the task specifies this function be defined as 'max', this causes a recursion error and so I have renamed to minimum
def maximum(list_of_numbers):
    return max(list_of_numbers)

# Defines a function that allows for calculating the sum number of a list of numbers
def sum(list_of_numbers):
    i = 0
    total = 0
    for i in list_of_numbers:
        total += i
    return total

# Defines a function that allows for calculating the correct element corresponding to the xth percentile of a list of numbers
def x_percentile(list_of_numbers, percentile_number):
    percentile_index_value = round(percentile_number*len(list_of_numbers)/100)
    return list_of_numbers[percentile_index_value - 1]

# Defines a function which calls the appropriate function listed in the input file
def select_func(func, list_of_numbers):
    if func == 'min':
        return minimum(list_of_numbers)
    elif func == 'max':
        return maximum(list_of_numbers)
    elif func == 'avg':
        return average(list_of_numbers)
    elif func == 'sum':
        return sum(list_of_numbers)
    elif func[0] == 'p':
        return x_percentile(list_of_numbers, int(func[1:]))

# Reads input file and extracts contents line by line, storing each line as elements in a list
with open("input2.txt", "r", encoding='utf-8-sig') as input_file: # Note: spefiying the encoding paramter allows for exclusion of the byte order mark "ufeff"
    input_file_contents = input_file.readlines()

# Cleanses lines from input file of any trailing/leading spaces and extracts the intended functions by taking the colon as a delimiter
# This allows to store each function as the list of numbers to be taken as arguments to that function as separate elements of a sub-list within a wider list
input_file_lines = []
for i in input_file_contents:
    input_file_lines.append(i.rstrip().split(":"))

# Extracts the list of functions and lists of numbers separately for use later
func_list = []
extract_list = []
for i in input_file_lines:
    # Loops through each sub list to extract the functions and store them in a list of functions
    func = i[0]
    func_list.append(func)
    # Loops through each sub list to extract the numbers, recasts them to integers and store them in a list of integer sublists
    extract = i[1].split(',')
    extract_int_list = [int(x) for x in extract] # Uses list comprehension for recasting
    extract_list.append(extract_int_list)

# Final output is written to an output file in the format specified by the task
with open("output2.txt", "w") as output_file:
    for i in range(0, len(func_list)):
        # Loops through all lines in input file, extracts the function name and integer list and selects appropriate user defined function
        if func_list[0][0] != 'p': # Condition for non-percentile functions
            output_file.write(f"The {func_list[i]} of {extract_list[i]} is {select_func(func_list[i], extract_list[i])}.\n")
        else: # Condition for percentile functions as different output wording required
            output_file.write(f"The {func_list[i][1:]}th percentile of {extract_list[i]} is {select_func(func_list[i], extract_list[i])}\n")

# The user is notified with a preview of the content of the output file by printing output content to the user
print("The following text below the line has been written to the file \"output.txt\":")
print('─'*80)
with open("output2.txt", "r") as output_file:
    output_file_contents = output_file.read()
    print(output_file_contents)
