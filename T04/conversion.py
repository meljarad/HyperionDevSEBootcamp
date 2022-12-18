# Initial variable declarations
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# Conversion of variable types
num1 = int(num1) # Recasting the variable from float to integer
num2 = float(num2) # Recasting the variable from integer to float
string2 = str(num3) # Recasting the variable from integer to string and assigning to a more descriptively named variable without overwriting the value of string1
num4 = int(string1) # Recasting the variable from string to integer and assigning to a more descriptively named variable

# Output of new variable types
print(f"{num1}\n{num2}\n{string2}\n{num4}") # Line breaks used to avoid retyping print statements

