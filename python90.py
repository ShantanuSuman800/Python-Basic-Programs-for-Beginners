"""Write a program to display the following pattern:
     0 
    01
   010
  0101
 01010"""
output = 0
for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(1,i+1):
        print(output,end="")
        if output==0:
            output=1
        else:
            output=0
    print()