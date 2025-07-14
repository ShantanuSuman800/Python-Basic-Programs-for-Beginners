#Write a program to Find the Sum of G.P Series
a = int(input("Enter the first number of the series:"))
r = int(input("Enter the common ratio:"))
n = int(input("Enter the total no. of series:"))
sum_ = 0
print("The Geometric Series is:",end = "")
for i in range(n):
    print(a,end= ",")
    sum_ += a
    a = a*r
print()
print("The sum of the given Geometric progression is:",sum_)