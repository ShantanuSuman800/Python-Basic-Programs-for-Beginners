#Python Program to Print all Integers that Aren't Divisible by Either 2 or 3 and lie between 1 and 50.

my_list = [] 

for i in range(1, 51): 
    if (i % 2 != 0 and i % 3 != 0): 
        my_list.append(i) 

print(my_list)