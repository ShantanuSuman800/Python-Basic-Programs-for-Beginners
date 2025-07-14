"""Write a Python function that accepts a hyphen-separated sequence of words as input and prints the 
words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items: green-red-yellow-black-white
Expected Result: black-green-red-white-yellow"""

def sort(items):
    items=[n for n in items.split('-')]
    items.sort()
    print('-'.join(items))
sort("green-red-yellow-black-white")