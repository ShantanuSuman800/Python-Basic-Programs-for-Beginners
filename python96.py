'''Write a program to display the following pattern:
        0
      1 0 1
    2 1 0 1 2
  3 2 1 0 1 2 3
4 3 2 1 0 1 2 3 4'''
n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(' ',end='')
    for j in range(i,-1,-1):
        print(j,end='')
    for j in range(1,i+1):
        print(j,end='')
    print()
 
print()