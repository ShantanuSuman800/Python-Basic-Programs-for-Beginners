#Write a program to Find the Sum of A.P Series
a = int(input("Enter the first number of the series:"))
d = int(input("Enter the common difference:"))
n = int(input("Enter the total no. of series:"))
sum_ = 0
print("The Arithmetic Series is:",end = "")
for i in range(n):
    print(a,end= ",")
    sum_ += a
    a = a+d
print()
print("The sum of the given Arithmetic progression is:",sum_)