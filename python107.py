"""Write a program to find the Sum of following Series:
[(1^1)/1!] + [(2^2)/2!] + [(3^3)/3!] + [(4^4)/4!] + [(5^5)/5!] + ... + [(n^n)/n!]"""
n = int(input("Enter the no. of times of the series:"))
sum_ = 0
fact = 1
for i in range(1,n+1):
    fact *= i
    a = (i**i)/fact
    sum_ += a
print("The series is as follows:[(1^1)/1!] + [(2^2)/2!] + [(3^3)/3!] + [(4^4)/4!] +.......+ [({}^{})/{}!]".format(n,n,n))
print("The sum of the series is:",sum_)