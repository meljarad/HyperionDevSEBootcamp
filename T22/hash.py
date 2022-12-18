#T22 TASK 2 - HASH.PY

# Initial declaration of country-capital city pairs using dictionary
countryMap ={'France': 'Paris',
             'Sweden': 'Stockholm',
             'Oman': 'Muscat',
             'Australia': 'Canberra'
             'Japan': 'Tokyo'
             }

# The following code reads 'Sweden' as a key
print(countryMap['Sweden'])

# IF 'SWEDEN' EXISTS AS A KEY IN "countryMap":
# This will return the corresponding value from the existing key-value pair: "Stockholm"

# IF 'SWEDEN' DOES NOT EXIST AS A KEY IN "countryMap":
# This will return a KeyError as it is attempting to access a dictionary key-value pair that is not present.
# This can be avoided by using the .get() method, hence countryMap.get('Sweden') will return 'None'.
