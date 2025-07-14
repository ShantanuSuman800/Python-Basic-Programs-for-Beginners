"""Write a program to display the following pattern:
0        0
01      10
010    010
0101  1010
0101001010"""
n=5
a='01'
for i in range(1,n+1):
    print((a*i)[:i]+'  '*(n-i)+((a*i)[:i])[-1::-1])

print()

