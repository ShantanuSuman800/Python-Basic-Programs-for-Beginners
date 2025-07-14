#Python Program to Eliminate repeated lines from a file
#open the file 
f = open("file.txt", "r") 

# read lines 
lines = f.readlines() 

# create an empty list to store unique lines 
unique_lines = [] 

# traverse for all lines 
for line in lines: 
	# check if line is already in list 
	if line not in unique_lines: 
		unique_lines.append(line) 

# open file in write mode 
f = open("file.txt", "w+") 

# write all unique lines in file 
for line in unique_lines: 
	f.write(line) 

# close the file 
f.close()