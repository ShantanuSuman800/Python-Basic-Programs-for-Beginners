#Write a program to determine whether the given number is a Harshad Number
n=int(input("enter number:"))
temp=n
s=0
while(n>0):
    a=n%10
    s=s+a
    n=n//10
if(temp%s==0):
    print("it is a harshad number")
else:
    print("it is not a harshad number")