#Write a program to print all prime numbers from 1-500.

print("All the prime numbers between 1 and 500 are:")
for num in range(1,501):
    count = 0
    for i in range(2,num):
        if num%i==0:
            count +=1
            break
    if (count==0) and (num!=0):
        print(num,end=",")