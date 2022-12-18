# T30 - EMAIL.PY
# Necessary libraries for generating random content/address(es) for initial test e-mail in inbox
import random
import string

# Class used to construct instances of single e-mails
class Email():
    # Initializes attributes as variables that relate to the e-mail
    def __init__(self, contents, from_address, to_address):
        self.has_been_read = False # An e-mail is marked as unread by default until it has been read
        self.contents = contents
        self.is_spam = False # An e-mail is not marked as spam until otherwise flagged
        self.from_address = from_address
        self.to_address = to_address

    #A llows for marking as 'read' or marking as 'spam' by reversing the default boolean assignments
    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

# A custom-defined function that adds a 'generated' e-mail to a given list based on contents, addresses and intended list (i.e. inbox/outbox)
def add_email(contents, sender_address, recipient_address, email_list):
    email = Email(contents, sender_address, recipient_address)
    email_list.append(email)
    return email

# A custom-defined function that generates counts for inbox (including unread and spam) and outbox
def get_count(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list):
    inbox_total_count = len(inbox_as_list)
    outbox_total_count = len(outbox_as_list)
    unread_mails_in_inbox_count = 0
    deleted_count = len(deleted_as_list)
    spam_mail_count = len(spam_as_list)

    # Prevents index error in case the user has deleted the test e-mail from the inbox
    if inbox_total_count != 0:
        for mail in inbox_as_list:
            if mail.has_been_read == False:
                unread_mails_in_inbox_count += 1
            if mail.is_spam == True: # Call the mark_as_spam method here
                spam_mail_count += 1

    # Returns for use in the main menu function, allowing for updated counts
    return inbox_total_count, unread_mails_in_inbox_count, outbox_total_count, deleted_count, spam_mail_count

# Used in the "search for e-mail by index" option in the main menu
def get_email(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list):
    # Try-except block constructed to ensure only a valid index can be accepted (i.e. numeric, in-range)
    while True:
        try:
            email_index = int(input("Enter the index of the e-mail in the list that you wish to search for:\n"))
            inbox_as_list[email_index].has_been_read = True
            break
        except ValueError:
            print("Error: invalid value. Please try again.")
        except IndexError:
            print("Error: index out of range. Please try again.")

    # Decision logic to retrieve e-mail contents
    if len(inbox_as_list) == 0:
        print("No e-mails in inbox.")
    elif email_index < len(inbox_as_list):
        print(f"\nE-MAIL AT INDEX {email_index}:\n{'─'*60}")
        print(f"From:\t\t{inbox_as_list[email_index].from_address}")
        print(f"To:\t\t\t{inbox_as_list[email_index].to_address}")
        print(f"Contents:\t{inbox_as_list[email_index].contents}\n{'─'*60}\n")
        delete(inbox_as_list, outbox_as_list, deleted_as_list, inbox_as_list[email_index], spam_as_list, email_index)
        # Decision logic to only prompt mark as spam option if e-mail is not deleted (this works for the test e-mail)
        if len(inbox_as_list) == 0:
            pass
        else:
            mark_spam_option(inbox_as_list[email_index], inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list)

# This allows for a user to mark an e-mail as spam
def mark_spam_option(email, inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list):
    # The user is offered the option of marking a particular e-mail as spam or not
    spam_response = ""
    while spam_response not in ["Y", "N"]:
        spam_response = input("Do you wish to mark this e-mail as spam? Enter \'Y\' or \'N\':\n").strip().upper()
        if spam_response == "Y":
            email.mark_as_spam()
            print(f"E-mail marked as spam and moved to Spam folder.")
            # Remove the e-mail from the inbox_as_list and add it to the spam list
            inbox_as_list.remove(email)
            spam_as_list.append(email)
            get_count(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list) # Call get_count with updated inbox...

# A custom-defined function that retrieves the unread e-mails
def get_unread_emails(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list):
    unread_emails = []
    count_list = get_count(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list)
    unread_inbox_count = count_list[1]
    # Check if there are any unread e-mails
    if unread_inbox_count == 0:
        print("You have no unread e-mails.")
    else:
        # If there are, generate a list of unread e-mails by extracting the unread e-mails from the inbox
        for mail in inbox_as_list:
            if mail.has_been_read == False:
                unread_emails.append(mail)
                mail.mark_as_read()
                unread_counter = 1
        print(f"You have {unread_inbox_count} unread e-mail(s):\n")
        # Print each unread e-mail one by one
        for mail in unread_emails:
            print(f"Unread E-mail {unread_counter}:")
            print(f"From:\t\t{mail.from_address}")
            print(f"To:\t\t\t{mail.to_address}")
            print(f"Contents:\t{mail.contents}\n{'─'*60}\n")
            unread_counter += 1
            # Ask the user if they want to check the next unread e-mail or not
            go_to_next_unread = ""
            while go_to_next_unread not in ["Y", "N"]:
                go_to_next_unread = input("Do you wish to read the next unread e-mail? Type \'Y\' or \'N\':\n").strip().upper()
                if go_to_next_unread == 'Y':
                    get_unread_emails(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list)
                    continue
                elif go_to_next_unread == 'N':
                    break
                else:
                    print("Error! Invalid entry, please try again.")
    return unread_emails

# A custom-defined function that retrieve the spam e-mails
def get_spam_emails(email_list):
    spam_emails = []
    spam_counter = 1
    # Loop through the spam list and print each spam e-mail one by one
    for mail in email_list:
        if mail.is_spam == True:
            print(f"SPAM E-MAIL {spam_counter}:\n{'─'*60}")
            print(f"From:\t\t{mail.from_address}")
            print(f"To:\t\t\t{mail.to_address}")
            print(f"Contents:\t{mail.contents}\n{'─'*60}")
            spam_counter += 1
    return spam_emails

# A custom-defined function that allows to compose a new e-mail to be sent
def send_new_email(author_address, outbox_as_list, inbox_as_list, deleted_as_list, spam_as_list):
    recipient = input("Enter the recipient e-mail address:\n")
    contents = input("Enter the contents of the e-mail:\n")
    new_outgoing_email = Email(contents, author_address, recipient)

    # Display email contents prior to confirmation of sending
    print(F"\nE-MAIL PREVIEW BEFORE SENDING:\n{'─'*60}")
    print(f"From:\t\t{new_outgoing_email.from_address}")
    print(f"To:\t\t\t{new_outgoing_email.to_address}")
    print(f"Contents:\t{new_outgoing_email.contents}\n{'─'*60}\n")

    # Prompt user to confirm whether they wish to send or discard (and subsequently move to deleted if so)
    confirm_send = ""
    while confirm_send not in ['Y', 'N']:
        confirm_send = input("Do you wish to send this e-mail? Type 'Y' or 'N':\n").strip().upper()
        if confirm_send == 'Y':
            print(f"E-mail successfully sent from {author_address} to {recipient}.")
            outbox_as_list.append(new_outgoing_email)
            get_count(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list)
        elif confirm_send == 'N':
            print("E-mail discarded and moved to Deleted folder.")
            deleted_as_list.append(new_outgoing_email)
        else:
            print("Error: invalid entry, please try again!")

# A custom-defined function that prints the e-mails in the outbox one-by-one
def view_outbox(outbox_as_list):
    outbox_counter = 0
    for mail in outbox_as_list:
        outbox_counter += 1
        print(f"\nOUTBOX E-MAIL {outbox_counter}:\n{'─'*60}")
        print(f"From:\t\t{mail.from_address}")
        print(f"To:\t\t\t{mail.to_address}")
        print(f"Contents:\t{mail.contents}\n{'─'*60}")

# A custom-defined function that deletes an e-mail
def delete(inbox_as_list, outbox_as_list, deleted_as_list, email, spam_as_list, email_index):
    # The user is offered the option of deleting the e-mail
    del_response = ""
    while del_response not in ["Y", "N"]:
        del_response = input("Do you wish to delete this e-mail? Enter \'Y\' or \'N\':\n").strip().upper()
        if del_response == "Y":
            inbox_as_list.remove(email)
            email_index -= 1
            deleted_as_list.append(email)
            print("Email deleted and moved to Deleted folder.")
            get_count(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list) # Call get_count with updated inbox_as_list
            break
        elif del_response == "N":
            print(f"E-mail not deleted.")
            break
        else:
            print("Error: invalid entry, please try again!")

# A custom-defined function that generates random e-mail contents
def generate_random_contents():
    # Generate a random integer between 0 and 50
    n = random.randint(20, 50)
    # Generate a random string of n characters
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    # Return the generated string
    return rand_str

# A custom-defined function that generates random e-mail sender address
def generate_random_sender_address():
    # Generate a random string of 7 characters
    rand_address = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "@mail.com"
    # Return the randomly generated e-mail address
    return rand_address

# Go to menu or exit function
def menu_or_exit():
    while True:
        print("Press enter to return to the main menu, or type \'e\' to exit:")
        reply = input("")
        if reply == "":
            break
        elif reply == "e":
            print("Closing program...")
            exit()
        else:
            print("Error: invalid selection, please try again!")

# Main menu
def main_menu(border_length, inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list):
    user_choice = ""
    while user_choice != "quit":
        # Print main menu in user-readable format
        print('─'*border_length, "\nE-MAIL SERVICE")
        inbox_count, unread_inbox_count, outbox_count, deleted_count, spam_count = get_count(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list)
        print(f"Inbox e-mails: {inbox_count}")
        print(f"Unread e-mails in inbox: {unread_inbox_count}")
        print(f"Outbox e-mails: {outbox_count}")
        print(f"Deleted e-mails: {deleted_count}")
        print(f"Spam e-mails: {spam_count}\n")
        print("Menu Options:")
        print("- Search inbox for specific e-mail by index: type 'search'")
        print("- View unread e-mails: type 'unread'")
        print("- View spam e-mails: type 'spam'")
        print("- Compose a new e-mail: type 'send'")
        print("- View sent e-mails: type 'outbox'")
        print("- Exit the e-mail service: type 'quit'\n")

        # Decision logic to execute functions based on initial user input
        user_choice = input("Type your selection below:\n")
        if user_choice == "search":
            test_email.mark_as_read()
            print(f"You have {inbox_count} e-mail(s) in your inbox.")
            if inbox_count != 0:
                get_email(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list)
            menu_or_exit()
        elif user_choice == "unread":
            get_unread_emails(inbox_as_list, outbox_as_list, deleted_as_list, spam_as_list)
            menu_or_exit()
        elif user_choice == "spam":
            if spam_count == 0:
                print("You have no spam e-mails.")
            else:
                print(f"You have {spam_count} spam e-mail(s):\n")
                get_spam_emails(spam_as_list)
                menu_or_exit()
        elif user_choice == "send":
            send_new_email(my_email_address, outbox_as_list, inbox_as_list, deleted_as_list, spam_as_list)
            menu_or_exit()
        elif user_choice == "outbox":
            if outbox_count == 0:
                print("You have no sent e-mails in your outbox.")
            else:
                view_outbox(outbox_as_list)
            menu_or_exit()
        elif user_choice == "quit":
            print("Closing program...")
            exit()
        else:
            print("Error: invalid menu selection, please try again!\n")

# Global variables defined for use throughout
border_length = 65 # Used for UI and readability purposes
## Empty lists used to store recieved, sent, deleted and marked as spam e-mails respectively
inbox = []
outbox = []
deleted = []
spam = []

# Used in case user wishes to send e-mail (assumes that  user is logged in with this e-mail address):
my_email_address = "mo.eljarad@gmail.com"

# Used to generate a single test e-mail that resides in the inbox initially
test_contents = generate_random_contents()
test_email_sender = generate_random_sender_address()
test_email = add_email(test_contents, test_email_sender, my_email_address, inbox)

# Primary function used as spine of program
main_menu(border_length, inbox, outbox, deleted, spam)
