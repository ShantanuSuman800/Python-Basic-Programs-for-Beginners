#Write a program to check if the given number is a Disarium Number
n=input("enter the number:")
f=len(n)
n=int(n)
temp=n
s=0
while(n>0):
    a=n%10
    s=s+(a**f)
    f=f-1
    n=n//10
if(temp==s):
    print("it is disarium number")
else:
    print("it is not a disarium number")
