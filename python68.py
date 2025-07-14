#Write a program to check whether a given Number is Palindrome or Not.
n=int(input("Enter any number: "))
temp=n
rev=0
while(n!=0):
    t=n%10
    rev=rev*10+t
    n=n//10
if(temp==rev):
    print("palindrome number")
else:
    print("not a palindrome number")