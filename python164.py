#Find length of a string in python (4 ways)


string = "cloudDevelop"
x = len(string)
print("The length of the given string is:",x)


string = "cloudDevelop"
length = 0
for x in string:
  length += 1
print("The length of the given string is:",length)


string = "cloudDevelop"
counter = 0
while string[counter:]:
	counter += 1
print(counter)


string = "cloudDevelop"
map(lambda x : 1 , string)



string = "cloudDevelop"
print(sum(map(lambda x : 1 , string)))