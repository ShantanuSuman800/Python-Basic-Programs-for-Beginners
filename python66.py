#Write a program to Calculate the value of nCr.
n=int(input("enter n:"))
r=int(input("enter r:"))
i=n-r
fact=1
while(n>0):
    fact=fact*n
    n=n-1
fact1=1
while(r>0):
    fact1=fact1*r
    r=r-1
fact2=1
while(i>0):
    fact2=fact2*i
    i=i-1
print(fact/(fact1*fact2))