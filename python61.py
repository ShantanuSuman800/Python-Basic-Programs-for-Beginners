#Write a program to Check whether a given Number is Perfect Number.
n=int(input("enter the number:"))
l=[]
for i in range(1,n):
    if(n%i==0):
        l.append(i)
s=0
for j in l:
    s=s+j
if(n==s):
    print("it is a perfect number")
else:
    print("it is not a perfect number")