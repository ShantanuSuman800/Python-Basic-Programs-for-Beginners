#Python Program to Form a New String where the First Character and the Last Character have been Exchanged

def exchange_val(my_string):
   return my_string[-1:] + my_string[1:-1] + my_string[:1]

my_string1 = input("enter string: ")
print("The string is :")
print(my_string1)
print("The modified string is :")
print(exchange_val(my_string1))