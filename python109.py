"""Write a program to print the following Series:
1, 2, 3, 6, 9, 18, 27, 54, ... upto n terms"""
n = int(input("Enter the no. of times the series should do:"))
a = 1
print(a,end=",")
for i in range(2,n+1):
    if i%2==0:
        a =a*2
    else:
        a = a* (3/2)
    print(a,end=",")