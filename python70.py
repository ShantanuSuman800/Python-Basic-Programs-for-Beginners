#Write a program to check weather a given number is prime number or not
num = int(input("Enter the number:"))
for i in range(2,num):
    if (num%i==0):
        print("The given number is not a Prime number")
        break
    else:
        print("The given number is a Prime number")
        break