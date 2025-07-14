"""Write a program to find the Sum of following Series:
(1^1) + (2^2) + (3^3) + (4^4) + (5^5) + ... + (n^n)"""
n = int(input("Enter the no. of times of the series:"))
sum_ = 0
for i in range(1,n+1):
    sum_+=(i**i)
print("The sum of the following series is:",sum_)
print("The series is as follows:(1^1) + (2^2) + (3^3) + (4^4) +.........+ ({}^{})".format(n,n))