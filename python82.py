"""Write a program to display the following pattern:
* * * * * * * * *
  * * * * * * *
   * * * * *
    * * *
      *"""
for i in range(5,0,-1):
    print(" "*(5-i)+(2*i-1)*"*")