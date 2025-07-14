#Write a program to find the greatest of three numbers using else if ladder.
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if (a>b and a>c):
    print("the greatest number is",a)
elif(b>c and b>a):
    print("the greatest number is",b)
else:
    print("the greatest number is",c)