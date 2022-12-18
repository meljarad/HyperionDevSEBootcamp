# T22 - OPTIONAL TASK

# Initial declaration of abbreviations dictionary for five common Internet acronyms
internet_abbreviations_dict = {'ASAP': 'As soon as possible',
                               'LOL': 'Laughing out loud',
                               'AFK': 'Away from keyboard',
                               'BRB': 'Be right back',
                               'OMG': 'Oh my God'
                               }

# Two more common internet acronyms are added to the dictionary
internet_abbreviations_dict['TTYL'] = 'Talk to you later'
internet_abbreviations_dict['GTG'] = 'Got to go'

# Prints top border, title and description to the user for readability and UI purposes
border_length = 100
print('─'*border_length, "\nINTERNET ACRONYM ABBREVIATION CHECKER")
print("This program will search our dictionary to find the full definition of common acronyms used on the Internet!\n")

# User is prompted to search for an abbreviation definition by typing one in
# Note use of .strip() and .upper() to standardize input case and cleanse trailing/leading spaces, allowing improved search functionality
user_inputted_abbreviation = input("Begin by searching for any abbreviation below:\n").strip().upper()

# Conditional logic used to return the full definition of the abbreviation if can be found in the dictionary, else the user is informed is cannot be found
if user_inputted_abbreviation in internet_abbreviations_dict.keys():
    print(f"\nResult:\nThe acronym \'{user_inputted_abbreviation}\' is short for \'{internet_abbreviations_dict.get(user_inputted_abbreviation)}\'.")
else:
    print("\nResult:\nAbbreviation not found.")

# Prints bottom border for UI purposes
print('─'*border_length)
