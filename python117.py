#Write a program to Find the Sum of two Binary Numbers.
def add_binary(a,b):
  # convert the given binary numbers to decimal
  decimal_a = int(a,2)
  decimal_b = int(b,2)
  # add the decimal numbers
  result = decimal_a + decimal_b
  # convert the result to binary
  result = bin(result)
  # remove the '0b' prefix
  result = result[2:]
  # return the result
  return result

# take two binary numbers as input
bin_a = input('Enter the first binary number: ')
bin_b = input('Enter the second binary number: ')

# call the add_binary function
result = add_binary(bin_a,bin_b)

# print the result
print('Sum of the two binary numbers is:', result)