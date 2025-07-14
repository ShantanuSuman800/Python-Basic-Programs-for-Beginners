#write a program to find area of a scalene triangle and right angle triangle
s=input("enter 1 to find area of scalene tringle and 2 for right angle triangle:")
if(s=="1"):
    a=float(input("enter the first side:"))
    b=float(input("enter the second side:"))
    c=float(input("enter the third side:"))
    d=(a+b+c)*0.5
    areas=(d*(d-a)*(d-b)*(d-c))**0.5
    print("area of scalene triangle is:",areas)
elif(s=="2"):
    base=float(input("enter the base:"))
    height=float(input("enter the height:"))
    arear=(base*height)*0.5
    print("the area of right angle triangle is:",arear)