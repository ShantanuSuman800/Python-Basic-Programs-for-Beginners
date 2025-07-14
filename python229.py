#Python Program to Multiply All the Items in a Dictionary
# Sample Dictionary 
my_dict = {'data1':100,'data2':-54,'data3':247}

# Multiplying items 
result = 1
for key in my_dict: 
	result = result * my_dict[key] 

# Printing the result 
print(result) 