# T07 OPTIONAL TASK 2 - DECIDING WHAT TO WEAR

# Declaration of booleans to inform decision logic of subsequent program
is_temp_exceeding_20C = True
is_weekend = True
is_sunny = True
# Prompts the user to input data by answering key questions:
temp_response = input("Is the temperature greater than 20 degrees? Enter \'yes\' or \'no\':\n")
is_temp_exceeding_20C = True if temp_response.lower().strip() == "yes" else False
weekend_response = input("Is it the weekend today? Enter \'yes\' or \'no\':\n")
is_weekend = True if weekend_response.lower().strip() == "yes" else False # Short form of one-line if statement notation is used. Note use of .lower() and .strip() functions to standardise user input and cleanse of trailing/leading spaces
sunny_response = input("Is it sunny today? Enter \'yes\' or \'no\':\n")
is_sunny = True if sunny_response.lower().strip() == "yes" else False
# Prints output to the user with recommended outfit constructed based on the value of the outfit variables below in each if-statement
top = "short-sleeved shirt" if is_temp_exceeding_20C else "long-sleeved shirt"
bottom = "shorts" if is_weekend else "jeans"
hat = " and a cap" if is_sunny else ""
print(f"Based on the answers you have given, our algorithm recommends you wear a {top} with {bottom}{hat}.")
