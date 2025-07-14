#Python Program that Displays which Letters are in the Two Strings but not in Both


s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)^set(s2))
print("The letters are:")
for i in a:
    print(i)