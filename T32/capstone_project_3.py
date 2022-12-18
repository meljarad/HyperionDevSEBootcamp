# CAPSTONE PROJECT 3
import tabulate # Used to present shoe list data in a tabulated view

# Class used to model a shoe
class Shoes:
    # Initialises various attributes related to the Shoe
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # Returns the cost of the shoes
    def get_cost(self):
        return self.cost
    # Returns the quantity of the shoes
    def get_quantity(self):
        return self.quantity
    # Returns a string representation of this class
    def __str__(self):
        return f"\'{self.product}\' from {self.country}, code {self.code}, cost £{self.cost: .2f}, quantity: {self.quantity} available"

# Function that prints border and title for UI and user readability purposes
def print_section_title(title):
    print(f"{'—'*100}\n{title}\n")

# Function that opens and reads inventory file, creates a list of  objects with this data and appends to shoes list
def read_shoes_data(item_list):
    # Prints border and title for UI and user readability purposes
    print_section_title("Importing inventory data from inventory file...")
    # Read data from the inventory file and write it to a local list
    with open('inventory.txt', 'r') as input_file:
        raw_data_list = input_file.readlines()
    # Remove first line (i.e. headers) and the linebreaks from each element using list comprehension
    raw_data_list = [element.rstrip().split(',') for element in raw_data_list]
    total_entries_count = len(raw_data_list) - 1 # Subtract one to exclude headers
    # Extract the headers from the list and use them to build a dictionary template to store information about a shoe
    shoe_dict_template = {}
    for header_as_element in raw_data_list[0]:
        shoe_dict_template[header_as_element] = None
    # Loop through the list of data and replace each element with a dictionary construction
    raw_data_list_as_dicts = []
    for line_as_element in raw_data_list:
        temporary_dict = shoe_dict_template.copy()
        for count, value in enumerate(line_as_element):
            temporary_dict[list(temporary_dict.keys())[count]] = value
        raw_data_list_as_dicts.append(temporary_dict)
    # Remove the first item from the list as this is just the headers and is not needed
    del raw_data_list_as_dicts[0]
    # Loop through the list of dictionaries, create an object based on the element dictionary and append it to shoe_list
    failed_item_list = [] # Used to store failed entries
    raw_data_list_as_dicts_final = [] # Used to store clean entries
    successful_import_count = 0
    failed_import_count = 0
    for dict in raw_data_list_as_dicts:
        # Try-except block used to insure that costs are represented and floats, quantities as integers
        try:
            shoe_object = Shoes(dict['Country'], dict['Code'], dict['Product'], float(dict['Cost']), int(dict['Quantity']))
            item_list.append(shoe_object)
            raw_data_list_as_dicts_final.append(dict)
            successful_import_count += 1
        except ValueError:
            failed_item_list.append(dict) # Appends failed entries in case needed for revisiting data correction
            failed_import_count += 1
    # Display the successfully imported entries
    print(f"{successful_import_count}/{total_entries_count} entries have been has successfully imported from the inventory file:")
    successful_import_table_headers = raw_data_list_as_dicts_final[0].keys()
    successful_import_table_data =  [[value for value in successful_item_dictionary.values()] for successful_item_dictionary in raw_data_list_as_dicts_final]
    print(tabulate.tabulate(successful_import_table_data, headers= successful_import_table_headers, tablefmt= 'grid'))
    # Display the failed entries (i.e. the lines that couldn't be imported due to erroneous values)
    print(f"\n{failed_import_count}/{total_entries_count} entries failed to import due to the presence of unexpected value types:")
    failed_item_table_headers = failed_item_list[0].keys()
    failed_item_table_data =  [[value for value in failed_item_dictionary.values()] for failed_item_dictionary in failed_item_list]
    print(tabulate.tabulate(failed_item_table_data, headers= failed_item_table_headers, tablefmt= 'grid'))
    print("Please double check the above entry(s) in the inventory file and ensure that values are of expected type.")
    return shoe_dict_template, raw_data_list_as_dicts_final

# Function that allows for data capture from user about shoe, creates an object then appends to shoe list
def capture_shoes(item_list, dictionary_template):
    # Prints border and title for UI and user readability purposes
    print_section_title("CAPTURE SHOES DATA")
    # Prompts user to enter a country name for the product
    while True:
        product_country = input("Enter the product country of origin:\n").title().strip()
        # Checks if country name contains numeric values
        contains_numbers = False
        for char in product_country:
            if char.isdigit() == True:
                contains_numbers = True
        if contains_numbers == True:
            print("Error: invalid entry. Country names cannot contain numbers.")
        else:
            break
    # Prompts user to enter a product code and name
    product_code = input("Enter the product code:\n").upper().strip()
    product_name = input("Enter the product name:\n").strip()
    # Prompts user to enter a product cost
    while True:
        # Try-except block used to ensure only float costs are entered
        try:
            product_cost = round(float(input("Enter the product cost:\n").strip()), 2)
            break
        except ValueError:
            print("Error: invalid entry. Cost value must be numeric.")
    # Prompts user to enter a product quantity
    while True:
        # Try-except block used to ensure only integer quantities are entered
        try:
            product_quantity = int(input("Enter the product quantity:\n").strip())
            break
        except ValueError:
            print("Error: invalid entry. Quantity value must be an integer.")
    # Create a shoe object based on the data captured from the user and append to the shoe list
    shoe_object = Shoes(product_country, product_code, product_name, product_cost, product_quantity)
    item_list.append(shoe_object)
    # Print a summary of addition to the user:
    table_headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity']
    table_content = [[product_country, product_code, product_name, product_cost, product_quantity]]
    print("The following data has been appended to the list of shoes:")
    print(tabulate.tabulate(table_content, headers= table_headers, tablefmt= 'grid'))
    # Offer user to exit or return to main menu
    exit_or_main_menu(item_list, dictionary_template)
# Function that iterates over the shoes list and prints the details of the shoes returned from the __str__ function or in a table format
def view_all(item_list, dict):
    # Prints border and title for UI and user readability purposes
    print_section_title("VIEW ALL AVAILABLE PRODUCT DATA")
    # Prepare table headers
    table_headers = ["#"] + list(dict.keys())
    # Creates table data by looping over the shoe objects and extracting the attribute instances to create a list of lists
    table_data_list = []
    row_id = 0
    for obj in item_list:
        row_id += 1
        temporary_list = [row_id]
        temporary_list.append(obj.country)
        temporary_list.append(obj.code)
        temporary_list.append(obj.product)
        temporary_list.append(obj.cost)
        temporary_list.append(obj.quantity)
        table_data_list.append(temporary_list)
    # Print the list of lists as a table
    print("The following records show all details for the list of shoe objects:")
    print(tabulate.tabulate(table_data_list, headers= table_headers, tablefmt= 'grid'))
    # Offer user to exit or return to main menu
    exit_or_main_menu(item_list, dict)
# Function to identify the shoe object with the lowest quantity, prompt user to restock and update records
def re_stock(item_list, dictionary):
    # Prints border and title for UI and user readability purposes
    print_section_title("UPDATE STOCK VALUE FOR LOWEST QUANTITY ITEM")
    # Loop through all shoes in shoe list and extract their ID and their quantity
    quantity_list = []
    content_list = {}
    for obj in item_list:
        quantity_list.append([id(obj), obj.quantity])
        content_list.update({id(obj): vars(obj)})
    # Obtain the ID of the object with the smallest quantity using a lambda function
    min_quantity_as_list = min(quantity_list, key=lambda x: x[1])
    min_quantity_obj_ID = min_quantity_as_list[0]
    # Generate a dictionary which stores minimum quantity product information
    min_quantity_obj_dict = content_list.get(min_quantity_obj_ID, 'None')
    # Generate a table of the object properties
    table_headers = list(dictionary.keys())
    table_content = [list(min_quantity_obj_dict.values())]
    # Print the minimum quantity object details to the user
    print("The following product has been identified has having the lowest inventory:\n")
    print(tabulate.tabulate(table_content, headers= table_headers, tablefmt= 'grid'))
    # Prompt user whether they wish to update the quantity value
    while True:
        update_or_not = input("Do you wish to update the quantity for this product? Type 'Y' or 'N':\n").upper().strip()
        # Constrains non-numeric replies to 'Y' or 'N'
        if update_or_not in ['Y', 'N']:
            break
        else:
            print("Error: invalid value. Please only enter 'Y' or 'N'.")
    # Prompts user to then enter the additional stock amount they wish to order
    while True:
        if update_or_not == 'Y':
            # Try-except block used to constrain additional quantity order to only allow integer quantities
            while True:
                try:
                    extra_quantity = int(input("Enter the additional quantity you wish to restock for this product:\n"))
                    break
                except ValueError:
                    print("Error: invalid value. Please only enter integer values for quantity restock orders.")
            # Loop through shoes list and find the object to update, then update the quantity value
            for obj in item_list:
                old_quantity = obj.quantity
                if id(obj) == min_quantity_obj_ID:
                    obj.quantity += extra_quantity
                    product_code = obj.code
                    break
            # Update the product record in the inventory file with the new quantity
            with open('inventory.txt', 'r+') as inventory:
                # Read in content from the inventory file
                inventory_list = inventory.readlines()
                temp_list = []
                # Split the contents in to list to make parsing the rows by values easier
                for i in inventory_list:
                    temp_list.append(i.split(","))
                # Overwrite the old file content with the updated inventory information
                inventory.seek(0)
                for t in temp_list:
                    # Once the product has been identified (by product code), update the quantity on file with the new quantity
                    if t[1] == product_code:
                        t[-1] = f"{obj.quantity}\n"
                    # Reconstruct the row in the format of the file by joining with comma
                    t = ",".join(t)
                    inventory.writelines(t)
            # Print confirmation of update to the user.
            min_quantity_obj_dict['quantity'] = old_quantity + extra_quantity
            table_content = [list(min_quantity_obj_dict.values())]
            print(f"Quantity updated with new information shown below:")
            table_content = [list(min_quantity_obj_dict.values())]
            print(tabulate.tabulate(table_content, headers= table_headers, tablefmt= 'grid'))
            break
        elif update_or_not.upper().strip() == 'N':
            break
        else:
            print("Error: invalid entry. Please try again!")
    # Offer user to exit or return to main menu
    exit_or_main_menu(item_list, dictionary)

# Function that searches for a shoe in a list using its code, returns the shoe object, and prints it.
def search_shoe(item_list, dictionary_template):
    # Prints border and title for UI and user readability purposes
    print_section_title("SEARCH FOR SHOE INFORMATION BY CODE")
    # Prompt user for a shoe code
    shoe_code = input("Enter the product code for the shoe you wish to search:\n").strip()
    # Iterate over objects and extract a dictionary of the product details based on matching the code
    product_details = {}
    found_count = 0
    for obj in item_list:
        if obj.code == shoe_code:
            found_count += 1
            product_details = vars(obj)
            # Generate a table of the object properties
            table_headers = [t.title() for t in list(product_details.keys())]
            table_content = [list(product_details.values())]
            # Print the object details to the user
            print(f"\nThe following product has been identified has for code \'{shoe_code}\':")
            print(tabulate.tabulate(table_content, headers= table_headers, tablefmt= 'grid'))
    # Display message to user if product info cannot be found
    if found_count == 0:
        print(f"Product information not found for product code \'{shoe_code}\'.")
    # Offer user to exit or return to main menu
    exit_or_main_menu(item_list, dictionary_template)

# Function that calculates the total value for each item.
def value_per_item(item_list, dictionary_template):
    # Prints border and title for UI and user readability purposes
    print_section_title("DISPLAY INVENTORY VALUE BY PRODUCT")
    # Iterate over objects and extract a list of the product details based on matching the code
    product_details = []
    for obj in item_list:
        product_details.append(vars(obj))
    # Iterate over all the dictionaries that represent each product and create a new key for derived value (= cost * quantity)
    row_id = 1
    table_content = []
    for p in product_details:
        p['Total Inventory Value'] = round(p['cost']*p['quantity'], 2)
        table_content.append([row_id] + list(p.values()))
        row_id += 1
    # Prepare table headers and content
    table_headers = ["#"] + [t.title() for t in list(product_details[0].keys())]
    # Print the object details to the user
    print(tabulate.tabulate(table_content, headers= table_headers, tablefmt= 'grid'))
    # Offer user to exit or return to main menu
    exit_or_main_menu(item_list, dictionary_template)

# Function that determines the product with the highest quantity and prints this shoe as being for sale.
def highest_qty(item_list, dictionary):
    # Prints border and title for UI and user readability purposes
    print_section_title("DISPLAY HIGHEST INVENTORY PRODUCT")
    # Loop through all shoes in shoe list and extract their ID and their quantity
    quantity_list = []
    content_list = {}
    for obj in item_list:
        quantity_list.append([id(obj), obj.quantity])
        content_list.update({id(obj): vars(obj)})
    # Obtain the ID of the object with the highest quantity using a lambda function
    max_quantity_as_list = max(quantity_list, key=lambda x: x[1])
    max_quantity_obj_ID = max_quantity_as_list[0]
    # Generate a dictionary which stores maximum quantity product information
    max_quantity_obj_dict = content_list.get(max_quantity_obj_ID, 'None')
    # Generate a table of the object properties
    table_headers = dictionary.keys()
    table_content = [list(max_quantity_obj_dict.values())]
    # Print the maximum quantity object details to the user
    print("The following product has been identified has having the highest inventory:")
    print(tabulate.tabulate(table_content, headers= table_headers, tablefmt= 'grid'))
    # Print this shoe as being for sale
    print(f"The \'{max_quantity_obj_dict['product']}\' ({max_quantity_obj_dict['code']}) is for sale at a cost of {max_quantity_obj_dict['cost']} currency units.")
    # Offer user to exit or return to main menu
    exit_or_main_menu(item_list, dictionary)

# Function to offer user exit or return to main menu
def exit_or_main_menu(item_list, dictionary_template):
    while True:
        print("Press enter to go to the main menu or type 'e' to exit:")
        reply = input("")
        # Decision logic to control whether to exit or return to main menu
        if reply == "":
            main_menu(item_list, dictionary_template)
            break
        elif reply == "e":
            exit_program()
            break
        else:
            print("Error: invalid entry. Please try again.")

# Function to quit the program
def exit_program():
    print("Closing program...")
    exit()

#==========Main Menu=============
def main_menu(item_list, dictionary_template):
    # Prints border and title for UI and user readability purposes
    print_section_title("MAIN MENU:")
    # Prompt user to select an option
    print("Select from the following options:\n")
    print("- CAPTURE SHOE DATA: Add new shoe objects to the shoe list. Type 'capture' to proceed.")
    print("- VIEW ALL PRODUCT DATA: View all records within the shoe list. Type 'view' to proceed.")
    print("- RESTOCK LOWEST INVENTORY: View shoes with lowest inventory level and restock if you wish. Type 'restock' to proceed.")
    print("- SEARCH FOR SHOE DATA: Search for shoe data by product code. Type 'search' to proceed.")
    print("- INVENTORY VALUE: View value of inventory per shoe. Type 'value' to proceed.")
    print("- VIEW HIGHEST INVENTORY: View shoes with highest inventory level. Type 'highest' to proceed.")
    print("- EXIT PROGRAM: Close the program entirely. Type 'exit' to proceed.\n")

    while True:
        user_input = input("Enter your selection below:\n").lower().strip()
        # Decision logic that executes function based on user input
        if user_input == 'capture':
            capture_shoes(item_list, dictionary_template)
        elif user_input == 'view':
            view_all(item_list, dictionary_template)
        elif user_input == 'restock':
            re_stock(item_list, dictionary_template)
        elif user_input == 'search':
            search_shoe(item_list, dictionary_template)
        elif user_input == 'value':
            value_per_item(item_list, dictionary_template)
        elif user_input == 'highest':
            highest_qty(item_list, dictionary_template)
        elif user_input == 'exit':
            exit_program()
        else:
            print("Error: invalid entry. Please re-enter an option!")

# This list is used to store a list of objects of shoes
shoe_list = [] # This list is used to store a list of objects of shoes
shoe_dictionary_template = {} # Used as a template for storing object information in a dictionary
raw_shoe_data_as_dictionaries = [] # Used to store all object information as a list of dicitonaries
shoe_dictionary_template, raw_shoe_data_as_dictionaries = read_shoes_data(shoe_list)

# Core spine of the program, executed through this function being called
main_menu(shoe_list, shoe_dictionary_template)

