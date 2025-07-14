#Write a program to find out L.C.M. of two numbers.
def lcm(x, y): 
  
    # choose the greater number 
    if x > y: 
        greater = x 
    else: 
        greater = y 
  
    while(True): 
        if((greater % x == 0) and (greater % y == 0)): 
            lcm = greater 
            break
        greater += 1
  
    return lcm 
  
# change the values of num1 and num2 for a different result 
num1 = int(input("num1: "))
num2 = int(input("num2: "))
  
# uncomment the following lines to take input from the user 
#num1 = int(input("Enter first number: ")) 
#num2 = int(input("Enter second number: ")) 
  
print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))