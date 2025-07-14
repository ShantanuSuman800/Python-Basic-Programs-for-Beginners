"""Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20"""
def sum_(lst1 =[8,2,3,0,7]):
    sum_=0
    for i in lst1:
        sum_+=i
    print("Sum of all the numbers in the list:",sum_)
sum_()