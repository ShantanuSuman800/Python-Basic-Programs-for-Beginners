#Python Program to Find the Smallest Divisor of an Integer.
def findSmallestDivisor(n): 
	
	# Find all divisors 
	# of the number 
	divisors = [ i for i in range(2, n + 1) 
				if n % i == 0] 
	
	# Return the minimum divisor 
	return min(divisors) 
	
# Driver Code 
n = int(input("num: "))
print(findSmallestDivisor(n))