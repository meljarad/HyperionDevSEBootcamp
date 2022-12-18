# T09 - OPTIONAL TASK

# User inputs initial package price and delivery distance (note use of .lower() and .strip() to cleanse input of trailing/leading spaces and standardize to lowercase to prevent errors
employee_type = input("What is the status of the employee? Type \"A\" for salesperson and \"B\" for manager.\n").lower().strip()

# Salesperson salary calculations
if employee_type == 'a':
    gross_sales = float(input("What is the employee gross sales?\n"))
    salesperson_fixed_salary = 2000
    commission_rate = 0.08
    salary = salesperson_fixed_salary + (gross_sales*commission_rate)
    print(f"The employee's salary for this month is {round(salary)}")
# Manager salary calculations
elif employee_type == 'b':
    hours_worked = float(input("What is the number of hours worked this month by the employee?\n"))
    manager_hourly_rate = 40
    salary = manager_hourly_rate * hours_worked
    print(f"The employee's salary for this month is {round(salary)}")
