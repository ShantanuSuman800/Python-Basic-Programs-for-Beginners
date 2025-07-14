#Write a program to calculate factorial of a given number using for loop and also using while loop.
a=int(input("enter the number:"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

fact=1
while(a>0):
    fact=fact*a
    a=a-1
print(fact)