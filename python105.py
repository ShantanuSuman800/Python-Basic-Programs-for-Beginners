"""Write a program to find the Sum of following Series:
(1!/1) + (2!/2) + (3!/3) + (4!/4) + (5!/5) + ... + (n!/n)"""
n = int(input("Enter the no. of times of series:"))
sum_ = 0
fact = 1
for i in range(1,n+1):
    fact *= i
    sum_ += fact/i
print("The series is as follows: (1!/1) + (2!/2) + (3!/3) + .......+(n!/n)")
print("the sum of the following series is:",sum_)