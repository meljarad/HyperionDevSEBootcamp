# T05 OPTIONAL TASK

fav_rest = input("Please enter the name of your favourite restaurant:\n") # Note this is not cast as any particular variable type, but this will be stored as a string anyway as the default input variable type
int_fav = int(input("Please enter your favourite integer:\n")) # But this is specifically cast as an integer type
print(fav_rest)
print(int_fav)

int_fav = int(fav_rest) # This will throw out a Value Error as you cannot pass the string into an int unless the string variable itself only contains a representation of an integer. The reverse would be acceptable however as string is the default variable type and so the variable "fav_rest" could theoretically string represent the value of "int_fav".
