#WAP to print all even numbers of a list using list comprehension.
list1 = [10, 21, 4, 45, 66, 93]
# using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]
print("Even numbers in the list: ", even_nos)