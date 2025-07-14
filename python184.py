#Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a
#Hyphen-Separated Sequence after Sorting them Alphabetically

n=input("enter the string: ") 
l=n.split('-') 
l.sort() 
print('-'.join(l)) 