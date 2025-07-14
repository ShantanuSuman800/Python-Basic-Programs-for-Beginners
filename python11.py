#write the program of area of trapezium rhombus and parallelogram
a=float(input("enter the one of parallel side:"))
b=float(input("enter the other parallel side:"))
h=float(input("enter the height:"))
area=((a+b)*h)/2
print("the area of trapezium is",area)

d1=float(input("enter the first diagonal:"))
d2=float(input("enter the other diagonal:"))
area1=(d1*d2)/2
print("area of the rhombus is",area1)

b1=float(input("enter the base:"))
h1=float(input("enter the height:"))
area2=b1*h1
print("area of parallelogram is",area2)