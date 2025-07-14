'''Write a program to display the following pattern:
    A
   BAB
  CBABC
 DCBABCD
EDCBABCDE'''
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    for j in range(i,0,-1):
        print(chr(64+j),end='')
    for j in range(2,i+1):
        print(chr(64+j),end='')
    print()
 
print()