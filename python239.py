#Python Program to obtain the line number in which given word is present
import re 
def find_line_number(file_name, word): 
	with open(file_name, 'r') as f: 
		for i, line in enumerate(f): 
			if word in line: 
				return i+1

file_name = 'test.txt'
word = 'Program'
num = find_line_number(file_name, word) 
print("Line number of given word is:", num)