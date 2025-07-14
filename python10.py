#write a program to calculate the volume and surface area of cone sphere and cylinder
r=float(input("enter the radius of cone:"))
l=float(input("enter the slant height of cone:"))
h=float(input("enter the height of cone:"))
pi=3.14
sa=pi*r*(l+r)
volume=(1/3)*pi*(r**2)*h
print("the surface area of cone is",sa)
print("the volume of cone is",volume)

r1=float(input("enter the radius of sphere:"))
sa1=4*pi*(r1**2)
volume1=(4/3)*pi*(r1**3)
print("the surafce area of sphere is",sa1)
print("the volume of sphere is",volume1)

r2=float(input("enter the radius cylinder:"))
h1=float(input("enter the height of cylinder:"))
sa2=2*pi*r2*(r+h1)
volume2=pi*(r2**2)*h1
print("the surafce area of cylinder is",sa2)
print("the volume of cylinder is",volume2)
