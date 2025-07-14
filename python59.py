#Write a program to count the sum of digits in the entered number.
n=int(input("enter number:"))
s=0
while(n>0):
    a=n%10
    s=s+a
    n=n//10
print(s)
