#Python Program to Find the Power of a Number Using Recursion

def power_(x,n):
    if n==0:
        return 1
    else:
        return x*power_(x,n-1)
x = int(input("Enter the number:"))
n = int(input("Enter the power:"))
print("Result = ",power_(x,n))