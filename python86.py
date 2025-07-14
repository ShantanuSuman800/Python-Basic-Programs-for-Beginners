"""Write a program to display the following pattern:
1
0 1 0
1 0 1 0 1
0 1 0 1 0 1 0"""
output = 1
for i in range(1,5):
    for j in range(0,2*i-1):
        print(output,end="")
        if output==1:
            output=0
        else:
            output=1
    print()