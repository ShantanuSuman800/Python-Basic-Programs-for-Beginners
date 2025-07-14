"""Write a program to find the Sum of following Series:
(1) + (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n)"""
n = int(input("Enter the no. of times of the series:"))
sum_ = 0
print("The series is as follows:",end="")
for i in range(1,n+1):
    print("(",end="")
    sum_ += (i*(i+1))/2
    for j in range(1,i+1):
        print(str(j),end ="+")
    print(")",end="+")
print()
print("The sum of the following series  is:",sum_)