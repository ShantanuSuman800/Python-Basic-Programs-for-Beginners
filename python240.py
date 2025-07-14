#Count number of lines in a text file in Python
file = open('text.txt', 'r')
lines = file.readlines()
number_of_lines = len(lines) 
print(number_of_lines)
file.close()
