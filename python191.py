#WAP to find min, max and average of elements of a list having numeric data
list2=[]
n = int(input("Enter the length of your list: "))
for i in range (1,n+1):
    a=int(input("Enter the %d number: " %i ))
    list2.append(a)
min=list2[0]
max=list2[0]
for i in range(1,n):
    if max<list2[i]:
        max=list2[i]
    if min>list2[i]:
        min=list2[i]
print(" %d is the biggest number " %max)
print(" %d is the smallest number " %min)
l=len(list2)
s=0
list1=list(map(int,list2))
for i in list1:
    s=s+i
print("average:",s/l)