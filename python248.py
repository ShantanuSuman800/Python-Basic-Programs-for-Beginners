#Python program to reverse the content of a file and store it in another file
# open a file in read mode
with open('file1.txt', 'r') as f:
    data = f.read()
 
# open another file in write mode
with open('file2.txt', 'w') as f:
    # write the reversed content
    f.write(data[::-1])