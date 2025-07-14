#Program to find second largest number in a list
str1=input("enter string: ")
lst = str1.split(",")
lst=list(map(int,lst))
'''list1 = input("num without spacing: ")
print("list with num as string:",[*list])'''
lst.sort() 

print("Second largest element is:", lst[-2])