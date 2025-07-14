#Python Program to Sum All the Items in a Dictionary

myDict = {'data1':100,'data2':-54,'data3':247}

total = 0

for i in myDict:
    total += myDict[i]

print("Sum of all items in the dictionary is:", total)

