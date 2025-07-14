#Python – Maximum and Minimum Kth elements in Tuple

test_tup = (5, 20, 3, 7, 6, 8)
print("The original tuple is : " + str(test_tup))
K = 2
test_tup = list(test_tup)
temp = sorted(test_tup)
res = tuple(temp[:K] + temp[-K:])
print("The extracted values : " + str(res))
