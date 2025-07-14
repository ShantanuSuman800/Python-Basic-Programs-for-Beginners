#Write a menu driven program for calculating area of different geometrical figures such as circle,square, rectangle, and triangle.
a=input("enter the figure of which the area you want to calculate:")
if(a=="circle"):
    r=float(input("enter radius:"))
    area_c=3.14*(r**2)
    print("the area of circle is {}".format(area_c))
if(a=="rectangle"):
    l=float(input("enter the length:"))
    b=float(input("enter the breadth:"))
    area_r=l*b
    print("the area of rectangle is {}".format(area_r))
if(a=="square"):
    a=float(input("enter the side:"))
    area_s=a**2
    print("area of square is {}".format(area_s))
if(a=="triangle"):
    a1=float(input("enter the first side:"))
    b1=float(input("enter the second side:"))
    c1=float(input("enter the third side:"))
    d1=(a1+b1+c1)*0.5
    areas=(d1*(d1-a1)*(d1-b1)*(d1-c1))**0.5
    print("area of triangle is {}".format(areas))