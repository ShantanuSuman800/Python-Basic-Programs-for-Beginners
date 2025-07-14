#Write a program to find the reverse of a given number.
n=int(input("Enter any number: "))
rev=0
while(n!=0):
    t=n%10
    rev=rev*10+t
    n=n//10
print("Reverse number = ",rev)