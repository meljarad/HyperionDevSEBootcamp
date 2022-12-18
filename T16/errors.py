#T16 - ERRORS.PY
#Note: all previous comments have been removed, hence any comments in this submission are my own original contributions

print("Welcome to the error program\n") # Syntax error fixed, Fixes 1, 2 (see summary for more detail)
# Fix 3 (see summary for more detail
ageStr = "24 years old"
age = int(ageStr[0:2]) # Syntax error fixed, Fixes 6, 7 (see summary for more detail)

print("I'm " + str(age) + " years old.") # Syntax and logic error fixed, Fixes 8, 9 (see summary for more detail)

three_and_a_half = 3.5 # Logical error fixed, Fix 9, (see summary for detail)
answerYears = age + three_and_a_half # Syntax and logical error fixed, Fixes 10, 11 (see summary for detail)
answerMonths = answerYears * 12 # Runtime error fixed, Fix 14

print("The total number of years: " + str(answerYears))  # Syntax/logical error fixed, Fixes 4, 12 (see summary for more detail)
print("In 3 years and 6 months, I'll be " + str(int(answerMonths)) + " months old") # Syntax error fixed, Fixes 5, 13 (see summary for more detail)

# SUMMARY OF FIXES
# Fix 1: SYNTAX - Missing brackets before and after speech marks on line 4 (line 6 in original code) have now been included
# Fix 2: SYNTAX - Missing brackets before and after speech marks. This line was deleted and "\n" appended to end of the word "program" in line 4 instead.
# Fix 3: SYNTAX - Pointless indents have been removed from lines 5 to 11 (lines 7 to 13 in original code).
# Fix 4: SYNTAX - Missing brackets before and after speech marks on line 13 (line 16 in original code) have now been included
# Fix 5: SYNTAX - Missing brackets before and after speech marks on line 15 (line 18 in original code) have now been included
# Fix 6: SYNTAX - '==' replaced with '=' as should be for variable declaration
# Fix 7: SYNTAX - Cannot recast whole string to int due to non-numeric chars, slicing used to extract '24'
# Fix 8: SYNTAX - Cannot concatenate recasted int as str without recasting back to str, hence str() used to recast back to string
# Fix 9: LOGICAL - Spaces added before and after the age to appear correct
# Fix 10: LOGICAL - "three" renamed to "three_and_a_half" and value changed to 3.5 in accordance with expected output
# Fix 11: SYNTAX - Pointless speech marks removed so that "three_and_a_half" is not stored as str
# Fix 12: SYNTAX/LOGICAL - Pointless speech marks removed before and after "answerYears" to print variable value and not a string
# Fix 13: RUNTIME/SYNTAX - The program will run up until this line unless "answerYears" and "answerMonths" recasted to strings to allow for concatenatioin in print statement
# Fix 14: RUNTIME - "answer" changed to "answerYears"
