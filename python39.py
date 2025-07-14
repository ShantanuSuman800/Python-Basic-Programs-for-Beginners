#Write a program to find the greatest of three numbers using Nested if.
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if(a>b):
    if(a>c):
        print("a is the greatest number")
elif(b>a):
    if(b>c):
        print("b is the greatest number")
else:
    print("c is the greatest number")