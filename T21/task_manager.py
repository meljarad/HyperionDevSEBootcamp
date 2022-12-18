# T21 - CAPSTONE PROJECT II: FILES

from datetime import datetime # Used to record current date when new tasks are assigned

# Allows for customisation of border length printed before each section as part of UI, for readability purposes
def print_border(length_of_border):
    print('─'*length_of_border)

# Prompts user to enter an initial username and password at the beginning
def login_screen(border_length):
    global current_username
    global current_password
    print('─'*border_length, "\nTASK MANAGER PROGRAM")
    print("\nEnter your username and password to begin:")
    current_username = input("Username:\n")
    current_password = input("Password:\n")

# Produces a dictionary of valid login credentials by reading the user.txt file
def generate_valid_credentials_dictionary():
    # Extracts contents of the file and converts to a local list, and declares empty dictionary to be used later
    with open('user.txt', 'r') as input_file:
        valid_credentials_list = input_file.readlines()
        valid_credentials_dict = {}
    # Loops through local list and extracts username and password, cleansing of any commas/spaces to produce a credentials dictionary
    for i in range(0, len(valid_credentials_list)):
        valid_credentials_list[i] = valid_credentials_list[i].split(",")
        valid_credentials_list[i][1] = valid_credentials_list[i][1].strip()
        valid_credentials_dict.update({valid_credentials_list[i][0]: valid_credentials_list[i][1]})
    return valid_credentials_dict

# Uses the generated credentials dictionary to check user credential validity rather than rereading from the file each time
def check_credentials_validity(username, password, valid_credentials_dict):
    unsuccessful_login_count = 0
    # 'global' allows for use of current username and password outside of the function
    global current_username
    global current_password
    # If an invalid username or password is provided, deny access
    while not(username in valid_credentials_dict.keys()) or password != valid_credentials_dict.get(username):
        # Different error messages provided depending on if username, password or both are incorrect
        if not(username in valid_credentials_dict.keys()):
            print_border(border_length)
            print(f"ACCESS DENIED - {unsuccessful_login_count + 1} ATTEMPT(S). UNAUTHORISED USERNAME. Please login using a valid username:")
            username = input(f"Username:\n")
            password = input("Password:\n")
            unsuccessful_login_count += 1
        elif password != valid_credentials_dict.get(username):
            print_border(border_length)
            print(f"ACCESS DENIED - {unsuccessful_login_count + 1} ATTEMPT(S). INVALID PASSWORD. Please login using valid credentials:")
            username = input(f"Username:\n")
            password = input("Password:\n")
            unsuccessful_login_count += 1
    # Only reaches this point if access credentials are valid
    print("ACCESS GRANTED - LOGIN SUCCESSFUL.")
    current_username = username # Note: this references a global variable
    current_password = password # Note: this references a global variable

# Function to allow registering new user credentials
def register_new_user(border_length, username, tasks_dict_template):
    print_border(border_length)
    # Conditional logic to prevent non-admins from registering new users
    if username != 'admin':
        print("Invalid selection. Only admin users can register new users.")
        main_menu(border_length, username, tasks_dict_template)
    else:
        print("r - NEW USER REGISTRATION")
        new_username = input("Enter the username you wish to register:\n")
        new_password = input(f"Enter desired password for user \'{new_username}\':\n")
        new_password_tbc = input(f"Re-enter desired password for user \'{new_username}\':\n")
        # Validation step to confirm that users know what password they are registering
        while new_password != new_password_tbc:
            print("ERROR - Passwords do not match.")
            new_password = input(f"Enter desired password for user \'{new_username}\':\n")
            new_password_tbc = input(f"Re-enter desired password for user \'{new_username}\':\n")
        update_valid_credentials_file(new_username, new_password, new_password_tbc)

# Writes back to 'user.txt' with newly registered credentials
def update_valid_credentials_file(user, pw, pw_conf):
    if pw == pw_conf:
        with open("user.txt", 'a') as valid_credentials_file:
            valid_credentials_file.writelines(f"{user}, {pw}\n")
            print(f"New user \'{user}\' successfully registered.")

# Allows to update the 'tasks.txt' file with newly added tasks
def add_new_task(border_length):
    print_border(border_length)
    # Prompts user to enter new task details
    print("a - ADD NEW TASKS")
    task_assignee = input(f"Enter the username of the person whom the task will be assigned to:\n")
    task_title = input(f"Enter the title of the task:\n")
    task_description = input(f"Enter the description of the task:\n")
    task_due_date = input(f"Enter the due date of the task (format: DD MMM YYYY):\n")
    # Writes newly inputted task details back to the "tasks.txt" file
    with open("tasks.txt", 'a') as valid_credentials_file:
        valid_credentials_file.writelines(f"{task_assignee}, {task_title}, {task_description}, {task_due_date}, {datetime.today().strftime('%d %b %Y')}, No\n")
    print(f"Task \'{task_title}\' successfully added.")

# Allows user to view already registered tasks by reading "tasks.txt"
def view_all_tasks(border_length, tasks_key_value_pair_template):
    print_border(border_length)
    print("va - VIEW ALL TASKS\n")
    # Reads "tasks.txt" and stores content in a local list
    with open("tasks.txt", "r") as input_file:
        tasks_file_list = input_file.readlines()
    # Stores each task in its own dictionary and stores all tasks in a wider list of dictionaries, each dictionary represent a single task
    task_dictionary_form_list = []
    for i in range(0, len(tasks_file_list)):
        tasks_file_list[i] = tasks_file_list[i].split(", ")
        tasks_file_list[i][-1] = tasks_file_list[i][-1].strip()
        tasks_key_value_pair_template.update({'Task Assignee': tasks_file_list[i][0], 'Task Title': tasks_file_list[i][1], 'Task Description': tasks_file_list[i][2], 'Task Due Date': tasks_file_list[i][3], 'Date Assigned': tasks_file_list[i][4], 'Task Completed?': tasks_file_list[i][5]})
        task_dictionary_form_list.append(tasks_key_value_pair_template.copy())
    # Loops through list of dictionaries [i.e. tasks] and prints them in a readable form to the user
    task_number = 1
    for i in range(0, len(task_dictionary_form_list)):
        print(f"Task Title:\t\t\t\t{task_number}. {task_dictionary_form_list[i].get('Task Title')}")
        print(f"Task Assignee:\t\t\t{task_dictionary_form_list[i].get('Task Assignee')}")
        print(f"Task Description:\t\t{task_dictionary_form_list[i].get('Task Description')}")
        print(f"Date Assigned:\t\t\t{task_dictionary_form_list[i].get('Date Assigned')}")
        print(f"Due Date:\t\t\t\t{task_dictionary_form_list[i].get('Task Due Date')}")
        print(f"Task Completed?:\t\t{task_dictionary_form_list[i].get('Task Completed?')}")
        task_number += 1
        print("-"*110) # Used to separate each task, for UI and readability purposes

# Similar to view_all_tasks() with filtering step - allows user to view only their own tasks where the assignee is the same as the username.
def view_my_tasks(border_length, tasks_key_value_pair_template):
    print_border(border_length)
    print("vm - VIEW MY TASKS\n")
    # Imports tasks into local lists by reading "tasks.txt" file
    with open("tasks.txt", "r") as input_file:
        tasks_file_list = input_file.readlines()
    # Stores each task in its own dictionary and stores all tasks in a wider list of dictionaries, each dictionary represent a single task
    task_dictionary_form_list = []
    for i in range(0, len(tasks_file_list)):
        tasks_file_list[i] = tasks_file_list[i].split(", ")
        tasks_file_list[i][-1] = tasks_file_list[i][-1].strip()
        tasks_key_value_pair_template.update({'Task Assignee': tasks_file_list[i][0], 'Task Title': tasks_file_list[i][1], 'Task Description': tasks_file_list[i][2], 'Task Due Date': tasks_file_list[i][3], 'Date Assigned': tasks_file_list[i][4], 'Task Completed?': tasks_file_list[i][5]})
        # Filters only tasks where the assignee name matches the current logged in user
        if tasks_file_list[i][0] == current_username:
            task_dictionary_form_list.append(tasks_key_value_pair_template.copy())
    # Loops through list of dictionaries [i.e. tasks] and prints them in a readable form to the user
    task_number = 1
    for i in range(0, len(task_dictionary_form_list)):
        print(f"Task Title:\t\t\t\t{task_number}. {task_dictionary_form_list[i].get('Task Title')}")
        print(f"Task Assignee:\t\t\t{task_dictionary_form_list[i].get('Task Assignee')}")
        print(f"Task Description:\t\t{task_dictionary_form_list[i].get('Task Description')}")
        print(f"Date Assigned:\t\t\t{task_dictionary_form_list[i].get('Date Assigned')}")
        print(f"Due Date:\t\t\t\t{task_dictionary_form_list[i].get('Task Due Date')}")
        print(f"Task Completed?:\t\t{task_dictionary_form_list[i].get('Task Completed?')}")
        task_number += 1
        print("-"*110) # Used to separate each task, for UI and readability purposes

# Allows user to select more than one option by returning to the main menu or exiting
def go_to_main_menu_or_exit(border_length, user, tasks_dict_template):
    menu_or_exit = input("Press enter to return to main menu or type 'e' to exit:\n")
    # Conditional logic to execute return to menu or exit program
    if menu_or_exit == '':
        main_menu(border_length, user, tasks_dict_template)
    elif menu_or_exit == 'e':
        exit_program()

# Allows user to 'log out' by exiting the program
def exit_program():
    print("INFO: You have successfully logged out.")
    exit()

# Provides menu functionality to the user, reliant on execution of previous functions based on user input
def main_menu(border_length, user, tasks_dict_template):
    print_border(border_length)
    print(f"You are logged in as \'{user}\'.")
    # Customises the output to show number of tasks and registered users to admins
    if user == 'admin':
        print("ADMIN MAIN MENU:") # Custom title
        # Generate a count of users by reading the number of lines in "tasks.txt"
        with open("user.txt") as users_file:
            user_count = len(users_file.readlines())
        # Generate a count of tasks by reading the number of lines in "tasks.txt"
        with open("tasks.txt") as tasks_file:
            tasks_count = len(tasks_file.readlines())
        # Display the number of tasks/users to the user
        print(f"Number of registered users: {user_count}")
        print(f"Number of added tasks: {tasks_count}\n")
    else:
        print("MAIN MENU:")
    # Prints list of available options to the user
    print("Please select one of the following options:")
    print("\tr - Registering a user")
    print("\ta - Adding a task")
    print("\tva - View all tasks")
    print("\tvm - View my tasks")
    print("\te - Exit")
    print("\nType your selection below:")
    menu_option = input().lower().rstrip() # Sanitises user input through use of .lower() and .strip()

    # Conditional logic used to excecute the appropriate function based on user input
    # REGISTERING A USER
    if menu_option == 'r':
        register_new_user(border_length, user, tasks_dict_template)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # ADDING A NEW TASK
    elif menu_option == 'a':
        add_new_task(border_length)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # VIEWING ALL TASKS
    elif menu_option == 'va':
        view_all_tasks(border_length, tasks_dict_template)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # VIEWING MY TASKS
    elif menu_option == 'vm':
        view_my_tasks(border_length, tasks_dict_template)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # EXITING THE PROGRAM
    elif menu_option == 'e':
        exit_program()

# Declaration of global variables used in multiple functions
border_length = 65 # Defines length of border printed before each section, for UI and readability purposes
# Defines a template for the fields of each task based on structure of "tasks.txt"
tasks_dict_template = {'Task Assignee': '', 'Task Title': '', 'Task Description': '', 'Task Due Date': '', 'Date Assigned': '', 'Task Completed?': ''}

# Generates a dictionary of users and passwords with permitted access
valid_credentials_dictionary = generate_valid_credentials_dictionary()
# Prompts user to log in with first username and password
login_screen(border_length)
# Double checks credentials access
check_credentials_validity(current_username, current_password, valid_credentials_dictionary)
# Core spine of this program
main_menu(border_length, current_username, tasks_dict_template)


