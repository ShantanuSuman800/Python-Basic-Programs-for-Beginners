"""Write a program to display the following pattern:
      *
     * *
    * * *
   * * * *
  * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *"""
for i in range(1,6):
    print(" "*(5-i)+"* "*(i))
for j in range(5,0,-1):
    print(" "*(5-j)+"* "*(j))