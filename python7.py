#write a program to calculate area of rectangular and square
a=int(input("enter the height:"))
b=int(input("enter the breadth:"))
area=a*b
if (a==b):
    print("area of square is",area)
else:
    print("area of rectangle is",area)