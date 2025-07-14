#Write a program to check weather an entered year is leap year or not.
a=int(input("enter the year:"))
if (a%400==0 or a%100==0):
    print("the year is leap year")
elif(a%4==0 and a%100!=0):
    print("the year is leap year")
else:
    print("the year is not a leap year")