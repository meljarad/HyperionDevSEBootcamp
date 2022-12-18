#T09 TASK 01 - COURIER.PY

# User inputs initial package price and delivery distance
package_price = float(input("Enter the price of the package you would like to send:\n"))
delivery_distance_km = float(input("Enter the total distance of the delivery (km):\n"))

# User uses binary string inputs to choose delivery options (note use of .lower() and .strip() to cleanse input of trailing/leading spaces and standardize to lowercase to prevent errors)
air_or_freight = input("Do you wish to send your package via air or freight? Type \'A\' for air delivery, \'B\' for freight:\n").lower().strip()
full_or_ltd_insurance = input("Do you wish to take out full insurance or limited insurance on your delivery? Type \'A\' for full insurance, \'B\' for limited insurance:\n").lower().strip()
is_gift = input("Is your delivery a gift or not? Type \"Y\" or \"N\":\n").lower().strip()
priority_or_std = input("Do you wish to send your delivery via priority delivery or standard delivery? Type \'A\' for priority delivery, \'B\' for standard delivery:\n").lower().strip()

# The following if statements are used as decision logic to select the correct costs for the final total cost tallying
if air_or_freight == 'a':
    freight_cost_centre = 0.36
elif air_or_freight == 'b':
    freight_cost_centre = 0.25

if full_or_ltd_insurance == 'a':
    insurance_cost_centre = 50
elif full_or_ltd_insurance == 'b':
    insurance_cost_centre = 25

if is_gift == 'y':
    gift_cost_centre = 15
elif is_gift == 'n':
    gift_cost_centre = 0

if priority_or_std == 'a':
    priority_cost_centre = 100
elif priority_or_std == 'b':
    priority_cost_centre = 20

total_cost = package_price + (delivery_distance_km*freight_cost_centre) + insurance_cost_centre + gift_cost_centre + priority_cost_centre

print(f"Your total delivery cost round to the nearest Rand is: R{round(total_cost)}")
