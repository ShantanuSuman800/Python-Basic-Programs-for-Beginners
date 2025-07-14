'''Write a program to display the following pattern:
1A2B3C4D5E
1A2B3C4D
1A2B3C
1A2B
1A'''
n=6
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(str(j)+chr(64+j),end='')
    print()
 
print()
