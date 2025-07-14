#Python Program to Take in a String and Replace Every Blank Space with Hyphen

def rep_(string):
    string=string.replace(" ","-")
    string=string.replace(" ","-")
    print("Modified string:")
    print(string)
a=input("enter string: ")
rep_(a)