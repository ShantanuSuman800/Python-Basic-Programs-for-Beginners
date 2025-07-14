"""Write a program to print the following sequence of integers. 
1, 2, 4, 8, 16, 32
"""
a = 1
for i in range(1,7):
    print(a,end=",")
    a*=2