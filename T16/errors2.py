#T16 - ERRORS2.PY
#Note: all previous comments have been removed, hence any comments in this submission are my own original contributions

animal = "lion" # Logical/syntax error, Fixes 2,5 (see summary for more detail)
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." # Logical syntax error fixed, Fixes 3, 4, 5 (see summary for more detail)

print(full_spec) # Syntax error, Fix 1 (see summary for more detail)

# SUMMARY OF FIXES
# Fix 1: SYNTAX - Missing brackets before and after variable name "full_spec"
# Fix 2: SYNTAX - Missing speech marks before and after variable value "Lion"
# Fix 3: LOGICAL/SYNTAX - Missing 'f' before speech marks added to convert string to f-string
# Fix 4: LOGICAL - The variables "animal_type" and "number_of_teeth" were swapped round after being in the wrong place
# Fix 5: LOGICAL - Minor punctuation corrections such as adding full stop at end of "full_spec" f-string and correcting "Lion" to "lion", ensuring grammatically correct output.
