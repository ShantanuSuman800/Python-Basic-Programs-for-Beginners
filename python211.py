#Python program to Find the size of a Tuple


gvntuple = (9, 11, 24, 19, 11, 23, 29, 23, 31)
tuplelength = len(gvntuple)
print('The length of the given tuple', gvntuple, 'is [', tuplelength, ']')



gvntuple = (9, 11, 24, 19, 11, 23, 29, 23, 31)
tuplelength = 0
for elemen in gvntuple:
    tuplelength = tuplelength+1
print('The length of the given tuple', gvntuple, 'is [', tuplelength, ']')
