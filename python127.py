#Write a Python function to find the Max of three numbers.
def max(a,b,c):
    if a>b:
        if a>c:
            print("{} is the maximum".format(a))
        else:
            print("{} is the maximum".format(c))
    else:
        if b>a:
            print("{} is the maximum".format(b))
        else:
            print("{} is the maximum".format(c))
x=int(input("enter number: "))
y=int(input("enter number: "))
z=int(input("enter number: "))
max(x,y,z)