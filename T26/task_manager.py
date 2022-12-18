# T26 - CAPSTONE PROJECT III: LISTS, FUNCTIONS AND STRING HANDLING

from datetime import datetime # Used to record current date when new tasks are assigned
import time
import os # Used to check filepath name

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
    # 'global' allows for use of current username and password outside function
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
def reg_user(border_length, username, tasks_dict_template):
    existing_credentials = generate_valid_credentials_dictionary() # Produces dictionary of existing credentials in "user.txt"
    print_border(border_length)
    # Conditional logic to prevent non-admins from registering new users
    if username != 'admin':
        print("Invalid selection. Only admin users can register new users.")
        main_menu(border_length, username, tasks_dict_template)
    else:
        print("r - NEW USER REGISTRATION")
        new_username = input("Enter the username you wish to register:\n")
        # Prevents admin from registering a duplicate user by checking if it is in the existing credentials dictionary
        while new_username in existing_credentials.keys():
            print(f"ERROR! Username \'{new_username}\' already exists.")
            new_username = input("Re-enter the username you wish to register:\n")
        # Validation step to confirm that users know what password they are registering
        new_password = input(f"Enter desired password for user \'{new_username}\':\n")
        new_password_tbc = input(f"Re-enter desired password for user \'{new_username}\':\n")
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
def add_task(border_length):
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

# Generates a list of tasks that stores each task into a dictionary
def generate_local_task_list(individual_task_as_dict_template):
    global local_task_list
    # Reads "tasks.txt" and stores content in a local list
    with open("tasks.txt", "r") as input_file:
        tasks_file_list = input_file.readlines()
    # Stores each task in its own dictionary and stores all tasks in a wider list of dictionaries, each dictionary represent a single task
    local_task_list = []
    task_id = 1
    for i in range(0, len(tasks_file_list)):
        tasks_file_list[i] = tasks_file_list[i].split(", ")
        tasks_file_list[i][-1] = tasks_file_list[i][-1].strip()
        individual_task_as_dict_template.update({'Task ID': task_id, 'Task Assignee': tasks_file_list[i][0], 'Task Title': tasks_file_list[i][1], 'Task Description': tasks_file_list[i][2], 'Task Due Date': tasks_file_list[i][3], 'Date Assigned': tasks_file_list[i][4], 'Task Completed?': tasks_file_list[i][5]})
        local_task_list.append(individual_task_as_dict_template.copy())
        task_id += 1

# Custom template used to print a list of tasks to the UI, can be used for all tasks or a certain user
def print_tasks_to_UI(task_list):
    # Loops through list of dictionaries [i.e. tasks] and prints them in a readable form to the user
    for i in range(0, len(task_list)):
        print(f"Task ID:\t\t\t\t{task_list[i].get('Task ID')}")
        print(f"Task Title:\t\t\t\t{task_list[i].get('Task Title')}")
        print(f"Task Assignee:\t\t\t{task_list[i].get('Task Assignee')}")
        print(f"Task Description:\t\t{task_list[i].get('Task Description')}")
        print(f"Date Assigned:\t\t\t{task_list[i].get('Date Assigned')}")
        print(f"Due Date:\t\t\t\t{task_list[i].get('Task Due Date')}")
        print(f"Task Completed?:\t\t{task_list[i].get('Task Completed?')}")
        print("-"*110) # Used to separate each task, for UI and readability purposes

# Allows user to view already registered tasks by reading "tasks.txt"
def view_all(border_length, individual_task_as_dict_template):
    print_border(border_length)
    print("va - VIEW ALL TASKS\n")
    # Generate list of tasks (1 task per dictionary)
    generate_local_task_list(individual_task_as_dict_template)
    print(local_task_list)
    # Loops through list of dictionaries [i.e. tasks] and prints them in a readable form to the user
    print_tasks_to_UI(local_task_list)

# Allows for editing task details within the programme and file
def edit_task_details(task_id_to_be_updated):
    global local_task_list
    global my_task_list
    task_to_be_updated_dict_template = {}
    # Copies the task to be updated into a single dictionary
    for i in local_task_list:
        if i["Task ID"] == task_id_to_be_updated:
            task_to_be_updated_dict_template = i.copy()
    print(f"The current value of \'{task_key_to_be_updated}\' for Task {task_id_to_be_updated} is: \"{task_to_be_updated_dict_template[task_key_to_be_updated]}\".")
    new_value = input(f"Enter the new value of \'{task_key_to_be_updated}\' for Task {task_id_to_be_updated}:\n")
    # Update the dictionary in list of dictionaries for all tasks and users tasks
    for i in local_task_list:
        if i["Task ID"] == task_id_to_be_updated: i[task_key_to_be_updated] = new_value
    for i in my_task_list:
        if i["Task ID"] == task_id_to_be_updated: i[task_key_to_be_updated] = new_value
    # Prepare list of dictionary values in format that can be rewritten to file
    full_list_of_tasks = []
    for i in local_task_list:
        task_in_list_form = []
        task_in_list_form.append(i["Task Assignee"])
        task_in_list_form.append(i["Task Title"])
        task_in_list_form.append(i["Task Description"])
        task_in_list_form.append(i["Task Due Date"])
        task_in_list_form.append(i["Date Assigned"])
        task_in_list_form.append(i["Task Completed?"])
        full_list_of_tasks.append(task_in_list_form)
        full_list_of_tasks.append("\n")
    # Write the new tasks to the tasks.txt file
    with open('tasks.txt', 'w') as tasks_file:
        for i in full_list_of_tasks:
            for j in range(0, len(i)):
                if j != (len(i) - 1):
                    tasks_file.writelines(str(i[j]) + ", ")
                else:
                    tasks_file.writelines(str(i[j]))

# Allows for marking a task as complete
def mark_task_complete(task_id_to_be_updated):
    global local_task_list
    global my_task_list
    task_to_be_updated_dict_template = {}
    # Copies the task to be updated into a single dictionary
    for i in local_task_list:
        if i["Task ID"] == task_id_to_be_updated:
            task_to_be_updated_dict_template = i.copy()
            task_key_to_be_updated = 'Task Completed?'
    # Update the dictionary in list of dictionaries for all tasks and users tasks
    for i in local_task_list:
        if i["Task ID"] == task_id_to_be_updated: i[task_key_to_be_updated] = "Yes"
    for i in my_task_list:
        if i["Task ID"] == task_id_to_be_updated: i[task_key_to_be_updated] = "Yes"
    # Prepare list of dictionary values in format that can be rewritten to file
    full_list_of_tasks = []
    for i in local_task_list:
        task_in_list_form = []
        task_in_list_form.append(i["Task Assignee"])
        task_in_list_form.append(i["Task Title"])
        task_in_list_form.append(i["Task Description"])
        task_in_list_form.append(i["Task Due Date"])
        task_in_list_form.append(i["Date Assigned"])
        task_in_list_form.append(i["Task Completed?"])
        full_list_of_tasks.append(task_in_list_form)
        full_list_of_tasks.append("\n")
    # Write the new tasks to the tasks.txt file
    with open('tasks.txt', 'w') as tasks_file:
        for i in full_list_of_tasks:
            for j in range(0, len(i)):
                if j != (len(i) - 1):
                    tasks_file.writelines(str(i[j]) + ", ")
                else:
                    tasks_file.writelines(str(i[j]))# Similar to view_all() with filtering step - allows user to view only their own tasks where the assignee is the same as the username.
    print(f"Task {task_id_to_be_updated}: \'{task_to_be_updated_dict_template['Task Title']}\' marked as complete.")

# Allows for editing a task assignee
def edit_task_assignee(task_id_to_be_updated):
    global local_task_list
    global my_task_list
    task_to_be_updated_dict_template = {}
    # Asks user for new assignee name
    new_assignee = input(f"Enter the username of the new Task Assignee for Task {task_id_to_be_updated}:\n")
    # Copies the task to be updated into a single dictionary
    for i in local_task_list:
        if i["Task ID"] == task_id_to_be_updated:
            task_to_be_updated_dict_template = i.copy()
            task_key_to_be_updated = 'Task Assignee'
    old_assignee = task_to_be_updated_dict_template[task_key_to_be_updated]
    # Update the dictionary in list of dictionaries for all tasks and users tasks
    for i in local_task_list:
        if i["Task ID"] == task_id_to_be_updated: i[task_key_to_be_updated] = new_assignee
    for i in my_task_list:
        if i["Task ID"] == task_id_to_be_updated: i[task_key_to_be_updated] = new_assignee
    # Prepare list of dictionary values in format that can be rewritten to file
    full_list_of_tasks = []
    for i in local_task_list:
        task_in_list_form = []
        task_in_list_form.append(i["Task Assignee"])
        task_in_list_form.append(i["Task Title"])
        task_in_list_form.append(i["Task Description"])
        task_in_list_form.append(i["Task Due Date"])
        task_in_list_form.append(i["Date Assigned"])
        task_in_list_form.append(i["Task Completed?"])
        full_list_of_tasks.append(task_in_list_form)
        full_list_of_tasks.append("\n")
    # Write the new tasks to the tasks.txt file
    with open('tasks.txt', 'w') as tasks_file:
        for i in full_list_of_tasks:
            for j in range(0, len(i)):
                if j != (len(i) - 1):
                    tasks_file.writelines(str(i[j]) + ", ")
                else:
                    tasks_file.writelines(str(i[j]))# Similar to view_all() with filtering step - allows user to view only their own tasks where the assignee is the same as the username.
    print(f"Task Assignee for Task {task_id_to_be_updated} has been changed from \'{old_assignee}\' to \'{new_assignee}\'.")

# Allows for editing a task assignee
def edit_task_due_date(task_id_to_be_updated):
    global local_task_list
    global my_task_list
    task_to_be_updated_dict_template = {}
    # Asks user for new assignee name
    new_due_date = input(f"Enter the new Due Date for Task {task_id_to_be_updated}:\n")
    # Copies the task to be updated into a single dictionary
    for i in local_task_list:
        if i["Task ID"] == task_id_to_be_updated:
            task_to_be_updated_dict_template = i.copy()
            task_key_to_be_updated = 'Task Due Date'
    old_due_date = task_to_be_updated_dict_template[task_key_to_be_updated]
    # Update the dictionary in list of dictionaries for all tasks and users tasks
    for i in local_task_list:
        if i["Task ID"] == task_id_to_be_updated: i[task_key_to_be_updated] = new_due_date
    for i in my_task_list:
        if i["Task ID"] == task_id_to_be_updated: i[task_key_to_be_updated] = new_due_date
    # Prepare list of dictionary values in format that can be rewritten to file
    full_list_of_tasks = []
    for i in local_task_list:
        task_in_list_form = []
        task_in_list_form.append(i["Task Assignee"])
        task_in_list_form.append(i["Task Title"])
        task_in_list_form.append(i["Task Description"])
        task_in_list_form.append(i["Task Due Date"])
        task_in_list_form.append(i["Date Assigned"])
        task_in_list_form.append(i["Task Completed?"])
        full_list_of_tasks.append(task_in_list_form)
        full_list_of_tasks.append("\n")
    # Write the new tasks to the tasks.txt file
    with open('tasks.txt', 'w') as tasks_file:
        for i in full_list_of_tasks:
            for j in range(0, len(i)):
                if j != (len(i) - 1):
                    tasks_file.writelines(str(i[j]) + ", ")
                else:
                    tasks_file.writelines(str(i[j]))# Similar to view_all() with filtering step - allows user to view only their own tasks where the assignee is the same as the username.
    print(f"Task Due Date for Task {task_id_to_be_updated} has been changed from \'{old_due_date}\' to \'{new_due_date}\'.")

# Custom defined function allowing users to see their own tasks
def view_mine(border_length, individual_task_as_dict_template, user):
    print_border(border_length)
    global local_task_list
    global my_task_list
    print("vm - VIEW MY TASKS\n")
    # Generate list of tasks (1 task per dictionary)
    generate_local_task_list(individual_task_as_dict_template)
    my_task_list = []
    # Filters the list to ensure only tasks assigned to user are included and writes to new tasklist
    for i in local_task_list:
        if i['Task Assignee'] == user: my_task_list.append(i)
    # Loops through list of dictionaries [i.e. tasks] and prints them in a readable form to the user
    print_tasks_to_UI(my_task_list)
    # Produce a list of the valid task IDs by extracting them from the list of local tasks
    valid_task_id_list = []
    for i in my_task_list:
        valid_task_id_list.append(i['Task ID'])
    # Offer user option of marking off a task as complete or editing task
    task_id_to_be_updated = int(input("Enter the ID of the task to be updated or enter -1 to return to the main menu.:\n"))
    # Obtain the index value of the task to be updated depending on where it sits in the local task list
    task_iterator = 0
    task_index = 0
    for i in my_task_list:
        if i['Task ID'] == task_id_to_be_updated:
            task_index = task_iterator
            break
        task_iterator +=1
    # Execute task updating based on user input
    if task_id_to_be_updated == -1:
        go_to_main_menu_or_exit(border_length, user, individual_task_as_dict_template)
    elif task_id_to_be_updated not in valid_task_id_list:
        print(f"Sorry! Task {task_id_to_be_updated} is an invalid selection.")
    elif my_task_list[task_index]['Task Completed?'] == 'Yes':
        print(f"Sorry! Task {task_id_to_be_updated} has already been marked as complete and cannot be updated.")
    else:
        print("Select an option from the below:")
        print(f"\t1. Mark task {task_id_to_be_updated} as \'Complete\'.")
        print(f"\t2. Edit Task Assignee or Task Due Date for task {task_id_to_be_updated}.")
        edit_option1 = int(input())
        if edit_option1 == 1:
            mark_task_complete(task_id_to_be_updated)
        elif edit_option1 == 2:
            print("Select an option from the below:")
            print(f"\t1. Edit Task Assignee for task {task_id_to_be_updated}.")
            print(f"\t2. Edit Task Due Date for task {task_id_to_be_updated}.")
            edit_option2 = int(input())
            if edit_option2 == 1:
                edit_task_assignee(task_id_to_be_updated)
            elif edit_option2 == 2:
                edit_task_due_date(task_id_to_be_updated)

# Allows user to select more than one option by returning to the main menu or exiting
def go_to_main_menu_or_exit(border_length, user, tasks_dict_template):
    menu_or_exit = input("Press enter to return to main menu or type 'e' to exit:\n")
    # Conditional logic to execute return to menu or exit program
    if menu_or_exit == '':
        main_menu(border_length, user, tasks_dict_template)
    elif menu_or_exit == 'e':
        exit_program()
    else:
        print("Invalid selection!")
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)

# Generates a task overview reports - "task_overview.txt"
def generate_task_overview_report(individual_task_as_dict_template):
    global local_task_list
    # Generate list of tasks (1 task per dictionary)
    generate_local_task_list(individual_task_as_dict_template)
    total_number_of_tasks = len(local_task_list)
    completed_task_list = []
    # Filters the list to ensure only completed tasks are included and writes to new completed tasklist
    for i in local_task_list:
        if i['Task Completed?'] == 'Yes': completed_task_list.append(i)
    total_number_of_completed_tasks = len(completed_task_list)
    total_number_of_incomplete_tasks = (total_number_of_tasks - total_number_of_completed_tasks)
    percentage_incomplete_tasks = round(total_number_of_incomplete_tasks*100/total_number_of_tasks, 2)
    # Calculates overdue incomplete tasks
    overdue_task_list = []
    # Checks if a task is overdue by comparing todays date and the due date epoch values:
    format_of_date = '%d %b %Y'
    for i in local_task_list:
        format_of_date = '%d %b %Y'
        due_date_epoch = datetime.strptime(str(i['Task Due Date']), format_of_date).timestamp()
        today_date_str = datetime.today().strftime(format_of_date)
        today_date_epoch = datetime.strptime(str(today_date_str), format_of_date).timestamp()
        if (i['Task Completed?'] == 'No') and (due_date_epoch < today_date_epoch):
            overdue_task_list.append(i)
    total_number_of_overdue_tasks = len(overdue_task_list)
    percentage_overdue_tasks = round(total_number_of_overdue_tasks*100/total_number_of_tasks, 2)
    # Constructs file content line by line
    task_overview_report_name = "task_overview.txt"
    title_1 = "TASK OVERVIEW\n"
    total_tasks_summary = f"\nTotal number of tasks: {total_number_of_tasks}"
    total_completed_tasks_summary = f"\nTotal number of completed tasks: {total_number_of_completed_tasks}"
    total_incomplete_tasks_summary = f"\nTotal number of incomplete tasks: {total_number_of_incomplete_tasks}"
    total_overdue_tasks_summary = f"\nTotal number of overdue tasks: {total_number_of_overdue_tasks}"
    percentage_total_tasks_summary = f"\nPercentage of total tasks that are incomplete: {percentage_incomplete_tasks}%"
    percentage_overdue_tasks_summary = f"\nPercentage of total tasks that are overdue: {percentage_overdue_tasks}%"

    tasks_overview_lines = [title_1,
                            total_tasks_summary,
                            total_completed_tasks_summary,
                            total_incomplete_tasks_summary,
                            total_overdue_tasks_summary,
                            percentage_total_tasks_summary,
                            percentage_overdue_tasks_summary,
                            ]
    # Writes content to the file and prints confirmation statement
    with open(task_overview_report_name, "w") as tasks_overview_file:
        tasks_overview_file.writelines(tasks_overview_lines)
    task_overview_filepath = os.path.abspath(f"mydir/{task_overview_report_name}")
    print(f"A summary of task overview has been successfully generated.\nPlease see \'{task_overview_filepath}\' for more details.")

# Custom defined function to produce a unique list of registered usernames
def generate_unique_user_list():
    global username_list_unique
    # Extract the user credentials from 'user.txt'
    with open("user.txt", "r") as user_file:
        user_file_content = user_file.readlines()
    # Extracting user list and not passwords
    username_list_unique = []
    for i in user_file_content:
        username_list_unique.append(i.split(',')[0])
    # Remove any duplicates to produce a clean list of unique registered users
    username_list_unique = list(dict.fromkeys(username_list_unique))

# Generates a user overview report - "user_overview.txt"
def generate_user_overview_report(individual_task_as_dict_template):
    global local_task_list
    global username_list_unique
    user_overview_report_name = 'user_overview.txt'
    # Calculate number of unique registered users
    generate_unique_user_list()
    total_number_of_registered_users = len(username_list_unique)
    # Calculate number of tasks in total
    generate_local_task_list(individual_task_as_dict_template)
    total_number_of_tasks = len(local_task_list)
    # Create a list of completed tasks:
    completed_task_list = []
    for i in local_task_list:
        if i['Task Completed?'] == 'Yes':
            completed_task_list.append(i)
    total_number_of_completed_tasks = len(completed_task_list)
    # Create a template of statistics per user
    user_stat_dict_template = {'Username': None,
                               'Total Tasks Assigned': 0,
                               'Total Tasks Assigned as Percentage of Total': 0,
                               'Percentage of Assigned Tasks Completed': 0,
                               'Percentage of Assigned Tasks Incomplete': 0,
                               'Percentage of Assigned Tasks Overdue': 0
                               }
    # Create a dictionary to act as a data structure storing all statistics using the username as a key:
    total_user_statistics_list = []
    for i in username_list_unique:
        user_stat_dict_template.update({'Username': i})
        total_user_statistics_list.append(user_stat_dict_template.copy())
    # Loop through total task list and update the total user statistics dictionary for any tasks found assigned to the user
    for i in local_task_list:
        for j in total_user_statistics_list:
            if i['Task Assignee'] == j['Username']:
                j['Total Tasks Assigned'] += 1
    # Update the total number of tasks as a percentage of total per user:
    for j in total_user_statistics_list:
        j.update({'Total Tasks Assigned as Percentage of Total': round(j['Total Tasks Assigned']*100/total_number_of_tasks, 2)})
    # Update the total number of completed tasks per user and then convert it to a percentage of their total assigned tasks
    for i in local_task_list:
        for j in total_user_statistics_list:
            if i['Task Assignee'] == j['Username'] and i['Task Completed?'] == 'Yes':
                j['Percentage of Assigned Tasks Completed'] += 1
    for j in total_user_statistics_list:
        if j['Total Tasks Assigned'] == 0:
            j.update({'Percentage of Assigned Tasks Completed': "N/A - No tasks assigned"})
            j.update({'Percentage of Assigned Tasks Incomplete': "N/A - No tasks assigned"})
        else:
            percentage_assigned_tasks_completed = float(round(j['Percentage of Assigned Tasks Completed']*100/j['Total Tasks Assigned'], 2))
            j.update({'Percentage of Assigned Tasks Completed': percentage_assigned_tasks_completed})
    # Update the total number of incomplete tasks per user as a percentage of their total assigned tasks
            percentage_assigned_tasks_incomplete = 100 - percentage_assigned_tasks_completed
            j.update({'Percentage of Assigned Tasks Incomplete': percentage_assigned_tasks_incomplete})
    # Calculate the assigned tasks per user that are overdue
        if j['Total Tasks Assigned'] == 0:
                    j.update({'Percentage of Assigned Tasks Overdue': "N/A - No tasks assigned"})
        else:
            for i in local_task_list:
                format_of_date = '%d %b %Y'
                due_date_epoch = datetime.strptime(str(i['Task Due Date']), format_of_date).timestamp()
                today_date_str = datetime.today().strftime(format_of_date)
                today_date_epoch = datetime.strptime(str(today_date_str), format_of_date).timestamp()
                if (i['Task Assignee'] == j['Username']) and (i['Task Completed?'] == 'No') and (due_date_epoch < today_date_epoch):
                    j['Percentage of Assigned Tasks Overdue'] += 1
            j['Percentage of Assigned Tasks Overdue'] = round(j['Percentage of Assigned Tasks Overdue']*100/j['Total Tasks Assigned'], 2)
    # Writes content to the file and prints confirmation statement
    with open(user_overview_report_name, "w") as user_overview_file:
        title = "USER OVERVIEW\n\n"
        user_overview_file.writelines(title)
        user_overview_file.writelines(f"Total number of registered users: {total_number_of_registered_users}\n")
        user_overview_file.writelines(f"Total number of tasks: {total_number_of_tasks}\n\n")
        # Writes values back to the file and appends % to the end if the value is an appropriate percentage figure
        for i in total_user_statistics_list:
            for j in i:
                if ('Percentage' in j.split(" ")):
                    if i.get(j) == "N/A - No tasks assigned":
                        user_overview_file.writelines(f"{j}: {i.get(j)}\n")
                    else:
                        user_overview_file.writelines(f"{j}: {i.get(j)}%\n")
                else:
                    user_overview_file.writelines(f"{j}: {i.get(j)}\n")
            user_overview_file.writelines("\n")
    user_overview_filepath = os.path.abspath(f"mydir/{user_overview_report_name}")
    print(f"\nA summary of user overview has been successfully generated.\nPlease see \'{user_overview_filepath}\' for more details.\n")

# Generates task and user overview reports
def generate_reports(border_length, individual_task_as_dict_template):
    print_border(border_length)
    print("gr - GENERATE REPORTS\n")
    generate_task_overview_report(individual_task_as_dict_template)
    generate_user_overview_report(individual_task_as_dict_template)

# Reads the output files and prints output to the user
def display_statistics(border_length, individual_task_as_dict_template):
    print_border(border_length)
    print("ds - DISPLAY STATISTICS\n")
    # Checks if the overview files already exist or not and generates them if not
    task_overview_report_name = "task_overview.txt"
    user_overview_report_name = "user_overview.txt"
    user_overview_filepath = os.path.abspath(f"{user_overview_report_name}").strip()
    task_overview_filepath = os.path.abspath(f"{task_overview_report_name}").strip()
    is_user_overview_file_existing = os.path.exists(user_overview_filepath)
    is_task_overview_file_existing = os.path.exists(task_overview_filepath)

    if (is_user_overview_file_existing == False) or (is_task_overview_file_existing == False):
        print("Generating reports first...")
        generate_user_overview_report(individual_task_as_dict_template)
        generate_task_overview_report(individual_task_as_dict_template)
    # Read from the files and print the output to the user
    print("-"*70)
    with open(task_overview_report_name, "r") as task_overview_report:
        task_overview_report_content = task_overview_report.readlines()
    for i in task_overview_report_content:
        print(i.rstrip())

    print("-"*70)
    with open(user_overview_report_name, "r") as user_overview_report:
        user_overview_report_content = user_overview_report.readlines()
    for i in user_overview_report_content:
        print(i.rstrip())

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
    print("\tgr - Generate reports")
    print("\tds - Display statistics")
    print("\te - Exit")
    print("\nType your selection below:")
    menu_option = input().lower().rstrip() # Sanitises user input through use of .lower() and .strip()

    # Conditional logic used to execute the appropriate function based on user input
    # REGISTERING A USER
    if menu_option == 'r':
        reg_user(border_length, user, tasks_dict_template)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # ADDING A NEW TASK
    elif menu_option == 'a':
        add_task(border_length)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # VIEWING ALL TASKS
    elif menu_option == 'va':
        view_all(border_length, tasks_dict_template)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # VIEWING MY TASKS
    elif menu_option == 'vm':
        view_mine(border_length, tasks_dict_template, user)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # GENERATE REPORTS
    elif menu_option == 'gr':
        generate_reports(border_length, tasks_dict_template)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # DISPLAY STATISTICS
    elif menu_option == 'ds':
        display_statistics(border_length, tasks_dict_template)
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)
    # EXITING THE PROGRAM
    elif menu_option == 'e':
        exit_program()
    else:
        print("ERROR: Invalid selection. Please try again!")
        go_to_main_menu_or_exit(border_length, user, tasks_dict_template)

# Declaration of global variables used in multiple functions
border_length = 65 # Defines length of border printed before each section, for UI and readability purposes
# Defines a template for the fields of each task based on structure of "tasks.txt"
tasks_dict_template = {'Task Assignee': '',
                       'Task Title': '',
                       'Task Description': '',
                       'Task Due Date': '',
                       'Date Assigned': '',
                       'Task Completed?': ''}

# Generates a dictionary of users and passwords with permitted access
valid_credentials_dictionary = generate_valid_credentials_dictionary()
# Prompts user to log in with first username and password
login_screen(border_length)
# Double checks credentials access
check_credentials_validity(current_username, current_password, valid_credentials_dictionary)
# Core spine of this program
main_menu(border_length, current_username, tasks_dict_template)


