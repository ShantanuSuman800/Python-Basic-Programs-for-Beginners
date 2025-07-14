#Write a program to Read a Coordinate Point and Determine its Quadrant.
x=int(input("enter x:"))
y=int(input("enter y:"))
if(x>0 and y>0):
    print("the coordinate is in first quadrant")
elif(x>0 and y<0):
    print("the coordinate is in fourth quadrant")
elif(x<0 and y>0):
    print("the coordinate is in third quadrant")
else:
    print("the coordinate is in third quadrant")