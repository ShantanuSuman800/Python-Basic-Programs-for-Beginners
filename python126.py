#Python program to find GCD between two given integer numbers
def gcd(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The GCD of", num1,"and", num2,"is", gcd(num1, num2))