"""Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336"""
def mul_(lst1):
    j=1
    for i in lst1:
        j=j*i
    print("Multiplication of all the numbers in the list:",j)
lst=[1,2,3,1,1]
mul_(lst)