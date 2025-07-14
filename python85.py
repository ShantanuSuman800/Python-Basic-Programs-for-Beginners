"""Write a program to display the following pattern:
A
B A B
A B A B A
B A B A B A B"""
output = "A"
for i in range(1,5):
    for j in range(0,2*i-1):
        print(output,end="")
        if output=="A":
            output="B"
        else:
            output="A"
    print()