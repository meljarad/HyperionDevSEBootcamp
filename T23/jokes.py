# T23 - TASK 2 - RANDOM JOKE GENERATOR

import random # Allows for use of random number generator functions

# List of 9 jokes declared below, setup and punchline separated using '#' as delimiter
jokes_list = ["I'm afraid for the calendar.#Its days are numbered!",
              "My wife said I should do lunges to stay in shape.#That would be a big step forward!",
              "Why do fathers take an extra pair of socks when they go golfing?#In case they get a hole in one!",
              "Singing in the shower is fun until you get soap in your mouth#Then it's a soap opera!",
              "What do a tick and the Eiffel Tower have in common?#They're both Paris sites!",
              "What do you call a fish wearing a bowtie?#So-fish-ticated!",
              "How do you follow Will Smith in the snow?#You follow the fresh prints!",
              "If April showers bring May flowers, what do May flowers bring?#Pilgrims!",
              "I thought the dryer was shrinking my clothes.#Turns out it was the refrigerator all along!"
              ]

# Generate a number between 0 and 8 (effectively randomly selects a joke by index)
random_int = random.randint(0, len(jokes_list) - 1)

# Split the joke into its setup and punchline components
setup = jokes_list[random_int].split("#")[0]
punchline = jokes_list[random_int].split("#")[1]

# Prints top border, title and description to the user for readability and UI purposes
border_length = 100
print('─'*border_length, "\nDAD JOKE GENERATOR")
print("This program will randomly generate a new dad joke each time!\n")

# Prompts the user to input if they want to hear a joke or not
# Note use of .strip() and .lower() to standardize input case and cleanse trailing/leading spaces
user_input = input("Do you want to hear a joke?\n\t- YES\n\t- NO\nType your reply below:\n").strip().lower()

print('─'*border_length) # Prints another top border for readability and UI purposes

# Conditional logic that delivers the punchline suspensefully or a message of condolence if the user has no sense of humour!
if user_input == 'yes':
    print(f"Q: \"{setup.upper()}...\"")
    punchline_reply = input("(Press any key for the punchline!)\n")
    print(f"A: ...\"{punchline.upper()}\"")
elif user_input == 'no':
    print("You're missing out :(")

print('─'*border_length) # Prints bottom border for readability and UI purposes
