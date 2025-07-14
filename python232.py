#Python Program to Map Two Lists into a Dictionary
# Program
list1 = [1, 2, 3, 4] 
list2 = ["a", "b", "c", "d"]
  
# Using zip() 
res = dict(zip(list1, list2)) 
  
# Printing result  
print ("Resultant dictionary is : " +  str(res))

