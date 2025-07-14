"""Write a program to display the following pattern:
A
B B
C C C
D D D D
E E E E E"""
for i in range(1,6):
    print((chr(64+i))*i)