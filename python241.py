#Python Program to remove lines starting with any prefix
#Given code

fname = input("Enter file name: ")
prefix = input("Enter prefix to remove: ")

#Solution

temp = []
with open(fname, 'r') as f:
    for line in f:
        if not line.startswith(prefix):
            temp.append(line)

with open(fname, 'w') as f:
    for line in temp:
        f.write(line)
