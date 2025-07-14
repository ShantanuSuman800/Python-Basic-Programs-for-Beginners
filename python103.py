"""Write a program to find the Sum of following Series:
1! + 2! + 3! + 4! + 5! + ... + n!"""
n = int(input("Enter the no. of times of the series:"))
sum_ = 0
if n== 0:
    fact = 1
fact = 1
for i in range(1,n+1):
    fact = fact*i
    sum_ += fact
print("The series is as follows:1!+2!+3!+......+{}!".format(n))
print("The sum of the following series is:",sum_)