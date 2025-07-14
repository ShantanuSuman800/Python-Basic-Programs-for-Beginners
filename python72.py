#Write a program to find the Sum of all prime numbers from 1-1000.

sum_ = 0
for num in range(1,1001):
    count = 0
    for i in range(2,num):
        if (num%i==0):
            count += 1
            break
    if count==0 and num!=0:
        sum_ += num
print("The sum of all prime number numbers from 1-1000 is:",sum_)