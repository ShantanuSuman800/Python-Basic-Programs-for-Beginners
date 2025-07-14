"""Write a program to find the Sum of following Series:
(1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n)"""
n = int(input("Enter the no. of times of the series:"))
sum_ = 0
print("The Series is as follows:",end="")
for i in range(1,n+1):
    print("("+str(i)+"*"+str(i)+")",end="+")
    sum_ += i*i
print()
print("The sum of the following series is:",sum_)