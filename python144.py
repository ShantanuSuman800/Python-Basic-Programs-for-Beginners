#Write a program to print Fibonacci Series using recursion

def fibonacci(n):
    if(n<2):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n = 5
for i in range(n):
    print("Fibonacci(",i,") = ",fibonacci(i))