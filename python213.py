#Create a list of tuples from given list having number and its cube in each tuple

list1 = [1, 2, 5, 6]
res = tuple(map(lambda x: (x, x**3), list1))
print(res)