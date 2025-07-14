#Write a program to convert an Upper-case character into lower case and vice-versa.
c=input("Enter any alphabet:")
if ord(c)>=65 and ord(c)<91:
    print(c.lower())
else:
    print(c.upper())