#Program to print all even numbers in a range
#Given range
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))

#Iterating each number in range
for i in range(lower,upper+1):

#Checking condition
    if(i%2==0):
        print(i,end=" ")