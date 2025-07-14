#Write a Python function that prints out the first n rows of Pascal's triangle.
def n_pascal(n):
    from math import factorial
# input n
    for i in range(n):
        for j in range(n-i+1):
 
        # for left spacing
            print(end=" ")
 
        for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
        # for new line
        print()
n_pascal(8)

print("************************************************************************************************************")

print("Nth row of Pascal's Triangle is:")
def getrow(n):
    a = 1
    print(a, end=" ")

    for i in range(1, n + 1):
        b = (a * (n - i + 1)) // i
        print(b, end=" ")
        a = b
getrow(8)