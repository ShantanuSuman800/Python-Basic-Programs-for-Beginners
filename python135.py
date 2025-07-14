#Write a Python function that takes a number as a parameter and check the number is prime or not.
def test_prime(n):
    if (n==1):
        print("The given number is Not prime")
    elif (n==2):
        print("The given number is a Prime number")
    else:
        for x in range(2,n):
            if(n % x==0):
                print("The given number is Not prime")
                break
            else:
                print("The given number is Prime")
                break
print(test_prime(2))