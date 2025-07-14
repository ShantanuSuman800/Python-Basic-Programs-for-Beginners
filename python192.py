#Program to check if element exists in list

def element_exists(lst, element):
  try:
    lst.index(element)
    return True
  except ValueError:
    return False
test_list = [1, 6, 3, 5, 3, 4]
 
print(element_exists(test_list, 3))
print(element_exists(test_list, 7))