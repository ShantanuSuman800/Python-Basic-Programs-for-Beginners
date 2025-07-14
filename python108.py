""" Write a program to find the Sum of following Series:
1/2 - 2/3 + 3/4 - 4/5 + 5/6 - ...... upto n terms"""
n = int(input("Enter the no. of times of the series:"))
sum_ = 0
for i in range(1,n+1):
    if i%2==0:
        sum_ -= i/(i+1)
    else:
        sum_ += i/(i+1)
print(sum_)