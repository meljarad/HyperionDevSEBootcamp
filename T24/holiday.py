# T24 - TASK 2 - HOLIDAY.PY

# User-defined function that calculates the total hotel cost (the product of nightly rate and number of nights)
def hotel_cost(no_of_nights):
    hotel_nightly_rate = 60
    total_hotel_cost = hotel_nightly_rate*no_of_nights
    return total_hotel_cost

# User-defined function that calculates the flight cost
def plane_cost(city_name):
    # Dictionary defined to store prices as values and destination names as keys
    destination_prices_dict = {'paris': 60,
                               'istanbul': 90,
                               'dubai': 250,
                               'new york': 350,
                               'singapore': 600
                               }
    # Looks up value against destination name taken as key
    if city_name in destination_prices_dict.keys():
        flight_cost = destination_prices_dict.get(city_name)
    return flight_cost

# User-defined function that calculates the total car hire cost (the product of daily rate and number of days)
def car_rental(no_of_days):
    car_day_rate = 30
    total_car_cost = car_day_rate*no_of_days
    return total_car_cost

# User-defined function that calculates the total holiday cost by calling on previous 3 functions
def holiday_cost(no_of_nights, city_name, no_of_days):
    total_holiday_cost = hotel_cost(no_of_nights) + plane_cost(city_name) + car_rental(no_of_days)
    return total_holiday_cost

# Prints top border, title and description to the user for readability and UI purposes
border_length = 100
print('─'*border_length, "\nHOLIDAY COST CALCULATOR")
print("This program will calculate the total cost of your holiday!\n")

# Prompts user to input a city choice by typing the city
print("Q1. Which city do you wish to visit? Select from the following by typing the city name from the list of available destinations:")
print("\t- Paris\n\t- Istanbul\n\t- Dubai\n\t- New York\n\t- Singapore")
destination_name = input().lower().strip() # Note use of .lower() and .strip() to standardize/cleanse input for better parsing

# Prompts user to input the number of nights they'll be staying and recasts as an integer
total_number_of_nights = int(input("Q2. How many nights do you intend to stay there?\n"))

# Prompts user to input the number of days they wish to hire a car if they intend to do so, else this value is set to 0
print("Q3. Do you intend to hire a car? Select from the following by typing 'Yes' or 'No:")
print("\t- Yes\n\t- No")
is_car_hired = input().lower().strip() # Note use of .lower() and .strip() to standardize/cleanse input for better parsing

if is_car_hired == 'yes':
    total_car_hire_days = int(input("Q4. How many days do you wish to hire a car for?\n"))
else:
    total_car_hire_days = 0

# Calculation of subtotals based on cost component and the total, by calling each function
total_flight_cost = round(plane_cost(destination_name), 2)
total_hotel_cost = round(hotel_cost(total_number_of_nights), 2)
total_car_cost = round(car_rental(total_car_hire_days), 2)
total_holiday_cost = round(holiday_cost(total_number_of_nights, destination_name, total_car_hire_days), 2)

# Prints a summary of the costs by breaking down each one to the user
print('─'*int(border_length*0.7), "\nCOST BREAKDOWN:\n") # Prints top border and title for readability and UI purposes
print("Destination:", "\t"*6, f"{destination_name.capitalize()}") # Note use of .capitalize() to ensure city name is capitalised when shown back to the user
print(f"TOTAL FLIGHT COST:", "\t"*5, f"£{total_flight_cost: .2f}")
print('─'*int(border_length*0.7)) # Prints another border

print("Hotel rate:", "\t"*6, f"£60.00 per night")
print("Number of nights:", "\t"*5, f"{total_number_of_nights} night(s)")
print(f"TOTAL HOTEL COST:", "\t"*5, f"£{total_hotel_cost: .2f}")
print('─'*int(border_length*0.7))

# Only prints breakdown of car hire cost if the user answered 'yes' to hiring a car
if is_car_hired == 'yes':
    print("Car hire day rate:", "\t"*5, f"£30.00 per day")
    print("Number of days:", "\t"*5, f"{total_car_hire_days} day(s)")
    print(f"TOTAL CAR HIRE COST:", "\t"*4, f"£{total_car_cost: .2f}")
    print('─'*int(border_length*0.7))

# Total cost is then finally printed to the user
print(f"TOTAL HOLIDAY COST:", "\t"*4, f"£{total_holiday_cost: .2f}")
