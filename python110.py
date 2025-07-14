""" Write a program to print the following Series:
2, 15, 41, 80, 132, 197, 275, 366, 470, 587"""
n=int(input("enter number: "))
s=2
print(s,end=",")
for i in range(1,n+1):
    s=(13*i)+s
    print(s,end=",")