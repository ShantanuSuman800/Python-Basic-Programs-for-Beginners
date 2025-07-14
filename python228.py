#WAP to create dictionary which has characters of given string as keys and frequency of characters as values. 
string = "abbcccddddeeeee"

d = {}

for i in string:
    d[i] = string.count(i)

print(d)