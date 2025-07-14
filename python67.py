#Write a program to generate the Fibonacci Series.
n=int(input("Enter end limit"))
a=0
b=1
s=0
for i in range(0,n):
    print(a,",",end="")
    s=a+b
    a=b
    b=s