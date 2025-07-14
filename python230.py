#Python Program to Remove the Given Key from a Dictionary
# Sample Dictionary 
sample_dict = { 
    'name' : 'John', 
    'age' : 27, 
    'designation' : 'Manager'
}

# Key to be removed 
key = 'age'

# Deleting the key 'age' 
del sample_dict[key] 

# Updated Dictionary 
print(sample_dict)