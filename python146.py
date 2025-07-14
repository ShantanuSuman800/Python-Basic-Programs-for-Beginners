#Write a program to Find Sum of Digits of the Number using Recursive Function.
def sum_of_digit( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))
print("The sum of the digits of {} is {}".format(123,sum_of_digit(123)))