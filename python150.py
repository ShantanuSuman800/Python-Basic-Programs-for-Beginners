#Python Program to Find the GCD of Two Numbers Using Recursion

def GCD(x,y):
    rem = x%y
    if rem==0:
        return y
    else:
        return(GCD(y,rem))
n = int(input("Enter the first number:"))
m = int(input("Enter the second number"))
print("GCD of numbers is",GCD(n,m))