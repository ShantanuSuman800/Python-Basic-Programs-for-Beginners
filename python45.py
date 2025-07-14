#Write a Program to find roots of a quadratic expression.
b=float(input("enter b:"))
a=float(input("enter a:"))
c=float(input("enter c:"))
s=-b+(((b**2)-4*a*c)**0.5)/2*a
s1=-b-(((b**2)-4*a*c)**0.5)/2*a
print("roots of the equation is",s,"and",s1)
