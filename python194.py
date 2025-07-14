#Program to Multiply all numbers in the list

str1=input("enter numbers separated by , :")
list1=str1.split(",")
print(list1)
list1=list(map(int,list1))
j=1
for i in list1:
    j=j*i
print(j)
