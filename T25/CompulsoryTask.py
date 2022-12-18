# T25 - COMPULSORY TASK

def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary.get(key)) # Fix 1 implemented (see summary of fixes below for more detail)

simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": 'd\'oh', # Fix 2 implemented (see summary of fixes below for more detail)
                         "maggie": " (Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) # Fix 3 implemented (see summary of fixes below for more detail)

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
# ------------------------
# SUMMARY OF FIXES:
# Fix 1: Corrected SyntaxError on line 5. Incorrect syntax written to get the value based on the key plus non-existing variable 'k' is referenced
# This was replaced with the correct method allowing for obtaining values based on an iterable list of dictionary keys

# Fix 2: Corrected SyntaxError on line 10, caused by missing escape backslash for the "'" character in value 'd'oh'
# This was fixed by including the escape backslash so that 'd'oh' --> 'd\'oh'

# Fix 3: Corrected TypeError on line 9, caused by keys listed as separate arguments rather than grouped as a list (as one argument)
# This was fixed by putting keys in square brackets to create one argument (i.e. 1 iterable list of keys) rather than 4 arguments (i.e. 4 individual keys)
