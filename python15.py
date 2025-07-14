#Write a program to Find the Gravitational Force Acting Between Two Objects.
G=6.67/(10**11)
m1=float(input("enter the mass of first object:"))
m2=float(input("enter the mass of second object:"))
r=float(input("enter the distance between two objects:"))
force=(G*m1*m2)/(r**2)
print("the force between two objects is",force)

