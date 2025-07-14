#Write a program to calculate sum of numbers 1 to N using recursion.

def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)
print("The sum of numbers from 1 to {} is {}".format(5,recurSum(5)))

