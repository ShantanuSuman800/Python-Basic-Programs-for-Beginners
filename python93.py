'''93. Write a program to display the following pattern:
A
B C
D E F
G H I J
K L M N O'''
s=64
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(s+j),end='')
    s=s+j
    print()
 
print()