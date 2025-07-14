#Python program to copy odd lines of one file to other
#open two files
with open('file1.txt', 'r') as f1, open('file2.txt', 'w') as f2:
    # read all lines into a list
    lines = f1.readlines()
    # iterate over the list and write only odd lines to file2
    for i, line in enumerate(lines):
        if i % 2 != 0:
            f2.write(line)
