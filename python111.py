""" Write a program to print the following Series:
1, 3, 4, 8, 15, 27, 50, 92, 169, 311"""
n = int(input("Enter the no.of times:"))
a = 1
b = 3
c = 4
print("The series is as follows:",end = "")
for i in range(1,n+1):
    if i==1:
        print(a,end = " ")
    elif i==2:
        print(b,end = " ")
    elif i==3:
        print(c,end = " ")
    else:
        d = a+b+c
        print(d,end=" ")
        a = b
        b = c
        c = d