#Write a program to Find the Sum of H.P Series
a = int(input("Enter the first number of the series:"))
d = int(input("Enter the common difference:"))
n = int(input("Enter the total no. of series:"))
sum_ = 0
print("The Harmonic Series is:",end = "")
for i in range(n):
    print(1/a,end= ",")
    sum_ += 1/a
    a = a+d
print()
print("The sum of the given Harmonic progression is:",sum_)