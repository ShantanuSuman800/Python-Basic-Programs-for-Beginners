"""Write a program to display the following pattern:
**********
**** ****
***  ***
**   **
*    *"""
for i in range(5,0,-1):
    print("*"*i+" "*(5-i)+"*"*i)