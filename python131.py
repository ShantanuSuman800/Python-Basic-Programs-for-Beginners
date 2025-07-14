"""Write a Python program calculate the factorial of a number using lambda and reduce functions. The 
function accepts the number as an argument."""
from functools import reduce

number = int(input('Enter number: '))

n = number

factorial = reduce(lambda x, y: x * y, range(1, n+1))

print('%d! = %d' %(number, factorial))