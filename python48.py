#Write a program to Simulate Arithmetic Calculator
a=int(input("enter number a:"))
b=int(input("enter number b:"))
c=input("enter the operator:")
if(c=="+"):
    print("the sum of a and b is {}".format(a+b))
if(c=="-"):
    print("the difference is {}".format(a-b))
if(c=="%"):
    print("the modulus is {}".format(a%b))
if(c=="/"):
    print("dividing a and b we get {}".format(a/b))
if(c=="//"):
    print("the floor division of a and b is {}".format(a//b))
if(c=="**"):
    print("the exponential is {}".format(a**b))
if(c=="*"):
    print("multiplying a and b we get {}".format(a*b))