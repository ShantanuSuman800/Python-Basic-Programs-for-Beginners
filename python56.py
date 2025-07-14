"""Write a program to print table of 5 in following format.
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15"""

for i in range(5,51):
    if(i%5==0):
        print("5 x {} = {}".format(i//5,i))
