# T06 OPTIONAL TASK
import math # Importing this library enables use of more efficient functions like .sqrt()

# Note: the formula used in line 12 only holds true only where the sum of any two sides exceeds the length of the third. This can be guarded against using while/if loops however they have not been taught yet and so I will not include them just yet. The purpose of this program is to demonstrate the capabilities of arithmetic operators and the imported 'math' library.
print("Triangle Area Calculator:\nNote: the sum of any two sides must always exceed the length of the third side, else this programme will crash!\n")

length1 = abs(float(input("Enter the length of the first side of the triangle:\n"))) # Abs() is used to ensure only positive values are used in the calculation
length2 = abs(float(input("Enter the length of the second side of the triangle:\n")))
length3 = abs(float(input("Enter the length of the third side of the triangle:\n")))

# Calculation of semiperimeter and area using Heron's formulae
semiperimeter = (length1 + length2 + length3)/2
area = math.sqrt(semiperimeter*(semiperimeter-length1)*(semiperimeter-length2)*(semiperimeter-length3))

# Output the area of the triangle to the user.
print(f"A triangle with sides of length {length1}, {length2} and {length3} has an area of {area: .3f}.")
