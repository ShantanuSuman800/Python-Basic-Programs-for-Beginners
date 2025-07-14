#Write a program using recursion to compute factorial of a given number
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print("The factorial of {} is {}".format(6,fact(6)))