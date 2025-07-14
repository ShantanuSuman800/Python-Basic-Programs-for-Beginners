#Write a program to Print Armstrong Number from 1 to 1000.
for i in range(1,1001):
    temp=i
    r=0
    while(i>0):
        n=i%10
        r=r+(n**3)
        i=i//10
    if(r==temp):
        print(temp)
    




