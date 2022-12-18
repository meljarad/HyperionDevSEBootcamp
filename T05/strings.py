# STRING SPLITTING AND JOINING
# Note: this program assumes no need to reuse variables and so conserves by rewriting to the same initially declared variable

hero = "Superman"
hero = list(hero.upper()) # We are unable to use the split function here without using a loop and iterating through the string to split at each index each time. The list function performs the same function without the need for writing a loop and addresses the issue of a lack of consistent delimiter availability. We use .upper() to convert ot upper case too
hero = "^".join(hero) # This line reassembles the string using a '^' character as a delimiter between each list element (i.e. each character)
print(hero) # Outputs the new desired format of "hero" to the user

