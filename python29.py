#Python program to compute the distance between the points (x1, y1) and (x2, y2)
x1=float(input("x1:"))
y1=float(input("y1:"))
x2=float(input("x2:"))
y2=float(input("y2:"))
distance=(((x1-x2)**2)+((y1-y2)**2))**0.5
print("the ditance between two points is:", distance)