#WAP to find the largest element in the list using reduce function

from functools import reduce

list1 = [-1, 3, 7, 99, 0]

print("The Largest element in the list is:")

print(reduce(lambda x, y: x if x > y else y,list1))