#Program to print all negative numbers in a range
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
for i in range(lower,upper):
    if i < 0:
        print(i)
