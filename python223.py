#Python Program to Concatenate Two Dictionaries into One.
# creating two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# concatenating two dictionaries
dict3 = {**dict1, **dict2}

# printing the result
print("Concatenated Dictionary:")
print(dict3)
