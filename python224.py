#Python Program to Check if a Given Key Exists in a Dictionary or Not
sample_dict = {'a': 1, 'b': 2, 'c': 3}
def check_key(dict_sample, key):
  if key in dict_sample.keys():
    return "Key Exists"
  else:
    return "Key Does not Exist"

key_input = 'c'
result = check_key(sample_dict, key_input)
print(result)