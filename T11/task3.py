# T11 - COMPULSORY TASK 3

# Prompts user to input their times for swimming, cycling and running components of triathlon
swimming_time_mins = float(input("Enter total swimming time in minutes:\n"))
cycling_time_mins = float(input("Enter total swimming time in cycling:\n"))
running_time_mins = float(input("Enter total swimming time in running:\n"))
total_time_taken = swimming_time_mins + cycling_time_mins + running_time_mins
qualifying_time = 100

# Decision logic using conditional if statements to determine what the appropriate award should be based on total time.
if total_time_taken <= qualifying_time:
    award = "Provincial Colours"
elif qualifying_time < total_time_taken < (qualifying_time + 5):
    award = "Provincial Half Colours"
elif (qualifying_time + 5) <= total_time_taken < (qualifying_time + 10):
    award = "Provincial Scroll"
else:
    award = "no award"

# Prints output to user stating what award they have been awarded based on above decision logic
print(f"\nBased on your total triathlon time of {total_time_taken} minutes, you have been awarded {award}.")
