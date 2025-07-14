#Python – Append content of one text file to another
# first open both files
f1 = open("file1.txt", "r")
f2 = open("file2.txt", "a")

# read the contents from the first file
content = f1.read()

# append the contents to the second file
f2.write(content)

# close both files
f1.close()
f2.close()