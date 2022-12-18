# T10 - TASK 2

print("BMI CALCULATOR")
# Prompts user to input weight and height details in order to calculate BMI
weight_kg = float(input("Please enter your weight in kilograms:\n"))
height_metres = float(input("Please enter your height in metres:\n"))
bmi_value = weight_kg / pow(height_metres, 2)

# If-else if-else statement use conditional logic to determine the user's BMI status based on their BMI value
if bmi_value >= 30:
    bmi_status = "obese"
elif 25 <= bmi_value < 30:
    bmi_status = "overweight"
elif 18.5 <= bmi_value < 25:
    bmi_status = "at a normal weight"
else:
    bmi_status = "underweight"

# Output a summary to the user
print(f"Your BMI is {bmi_value:.2f}, which means you are {bmi_status}.")
