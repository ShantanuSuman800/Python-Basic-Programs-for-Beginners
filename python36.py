#Write a program to Check if a given Integer is Positive or Negative and Odd or Even. 
a=int(input("enter the number:"))
if (a>0):
    print("a is a positive number")
else:
    print("a is a negative number")
if(a%2==0):
    print("a is an even number")
else:
    print("a is an odd number")