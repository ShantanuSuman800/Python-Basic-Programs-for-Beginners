#Python program to read character by character from a file
f = open('myfile.txt','r') 
for line in f: 
    for c in line: 
        print(c) 
   
f.close()
