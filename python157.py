#WAP to compute the cube of all numbers in the given list using map() function

l = [1, 2, 3, 4]
  
res = list(map(lambda x: x ** 3, l))
print(res)