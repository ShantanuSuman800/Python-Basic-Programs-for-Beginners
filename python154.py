#Python Program to Reverse a String Using Recursion.

def rev_str(str):
    l_str = len(str)
    if l_str==1:
        return str
    else:
        return rev_str(str[1:])+str[0]
x = input("Enter a string:")
print("The given string is:",x)
print("The reversed string is:",rev_str(x))