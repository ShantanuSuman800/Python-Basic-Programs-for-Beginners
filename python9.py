#write a program to find the volume and surface area of cube cuboids and cylinder
length=float(input("enter the side of cube:"))
sa=6*length*length
volume=length**3
print("the surface area of cube is",sa)
print("the volume area of cube is",volume)

length1=float(input("enter the length of cuboid:"))
breadth=float(input("enter the breadth of cuboid:"))
height=float(input("enter the height of cuboid:"))
sa1=2*((length1*breadth)+(breadth*height)+(height*length1))
volume1=length1*breadth*height
print("the surface area of cuboid is",sa1)
print("the volume of cuboid is",volume1)

r=float(input("enter the radius cylinder:"))
h=float(input("enter the height of cylinder:"))
pi=3.14
sa2=2*pi*r*(r+h)
volume2=pi*(r**2)*h
print("the surafce area of cylinder is",sa2)
print("the volume of cylinder is",volume2)
