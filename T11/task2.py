# T11 - COMPULSORY TASK 2
import math # Allows for use of pi value in circular area calculation via math.pi function

# Prompts user to input shape of building based
building_shape = int(input("1. Square\n2. Rectangular\n3. Round\n\nBased on the options above, enter the shape of your building foundation from the following selection:\n"))

# Calculates area based on user input if the area is a square shape
if building_shape == 1:
    square_side_length = float(input("Enter the length of the side of your building:\n"))
    area = pow(square_side_length,2)
    print(f"The foundation of the building will occupy a unit area of {area:.4f}.")
# Calculates area based on user input if the area is a rectangle shape
elif building_shape == 2:
    rectangle_length = float(input("Enter the length of the side of your building:\n"))
    rectangle_width = float(input("Enter the width of the side of your building:\n"))
    area = rectangle_width*rectangle_length
    print(f"The foundation of the building will occupy a unit area of {area:.4f}.")
# Calculates area based on user input if the area is a circular shape
elif building_shape == 3:
    circle_radius = float(input("Enter the radius of the circular foundation:\n"))
    area = math.pi*pow(circle_radius,2)
    print(f"The foundation of the building will occupy a unit area of {area:.4f}.")
# Prompts user to rerun program based on one of the three valid selections
else:
    print("Error: invalid selection. Please re-run proram and try again!")
