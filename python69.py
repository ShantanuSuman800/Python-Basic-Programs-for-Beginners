#Write a program to Check whether a given Number is an Armstrong Number
num = int(input("Enter the number:"))
n = num
order = len(str(n))
s = 0
while n>0:
    r = n%10
    s = s+r**order
    n = n//10
if (s==num):
    print("The given number is an Armstrong number")
else:
    print("The given number is not an Armstrong number")