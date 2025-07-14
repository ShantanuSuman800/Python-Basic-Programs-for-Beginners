#Python – Flatten tuple of List to tuple


test_tuple = ([5, 6], [6, 7, 8, 9], [3])
print("The original tuple : " + str(test_tuple))
res = tuple(sum(test_tuple, []))
print("The flattened tuple : " + str(res))


test_tuple = ([5, 6], [6, 7, 8, 9], [3])
print("The original tuple : " + str(test_tuple))
res = []
for i in test_tuple:
    for j in i:
        res.append(j)
res = tuple(res)
print("The flattened tuple : " + str(res))