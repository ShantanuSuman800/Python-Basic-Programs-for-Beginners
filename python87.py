'''Write a program to display the following pattern:
A B C D E F G F E D C B A
A B C D E F  F E D C B A
A B C D E      E D C B A
A B C D          D C B A
A B C              C B A
A B                  B A
A                      A'''
n=7
for i in range(0,n+1):
    for j in range(1,n-i+1):
        print(chr(64+j), end='')
    for j in range(1,2*i):
        print(' ', end='')
    for j in range(n-i,0,-1):
        if(j!=n):
            print(chr(64+j), end='')
    print()