#Program to Remove multiple elements from a list in Python
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
for i in list(li):
    f=int(input("enter element you want to remove:"))
    if f==0:
        break
    elif i//f==1:
        li.remove(i)
print("List after removing elements ",li)