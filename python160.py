#WAP to compute the sum of all the elements of the list using reduce() function

from functools import reduce

# List of some fibonacci numbers 
fiboList = [0,1,1,2,3,5,8,13,21,34,55]
print("List of fibonacci numbers :",fiboList)

 
listSum = reduce(lambda a,b:a+b,fiboList)
print("The sum of all elements is ",listSum)