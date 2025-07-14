#Write a program to print table of any number
n=int(input("enter the number:"))
for i in range(1,(n*10)+1):
    if(int(i)%n==0):
        print(i)