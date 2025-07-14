#Python Program that Displays which Letters are in the First String but not in the Second string






a = input("enter string:")
b = input("enter string:")
result=set()
for i in a:
	if i not in b:
		result.add(i)
print(result)