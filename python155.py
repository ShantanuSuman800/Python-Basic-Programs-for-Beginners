#WAP to convert a list of string type numbers into list of integer type numbers using map function.Ex: Input: [‘45’,’88’,’9’] Output:[45,88,9]

test_list = ['24', '45', '78', '40']
new_list=list(map(int,test_list))
print(new_list)