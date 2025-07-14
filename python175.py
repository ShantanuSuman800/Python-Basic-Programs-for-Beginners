#Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = input("enter string: ")
modified_str = ''
for char in range(0, len(str)):
    str = str.lower()
    if(str[char] == 'a'):
        modified_str += '$'
    else:
        modified_str += str[char] 
print("Modified string : ")
print(modified_str)